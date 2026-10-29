
import pytest

from highway_toll import toll_for, toll_charge, pass_advice


def test_invalid_axle_count():
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(1, False, False)


def test_base_tolls_for_supported_axle_counts():
    assert toll_for(2, False, False) == 100
    assert toll_for(3, False, False) == 150
    assert toll_for(4, False, False) == 250


def test_fallback_toll_for_other_valid_axle_counts():
    assert toll_for(5, False, False) == 400


def test_peak_hour_toll():
    assert toll_for(2, True, False) == 125


def test_fastag_discount_for_two_axles():
    assert toll_for(2, False, True) == 90


def test_fastag_discount_for_other_axle_counts():
    assert toll_for(3, False, True) == 142.5


def test_peak_and_fastag_combination():
    assert toll_for(2, True, True) == 112.5


def test_exempt_fire_engine():
    assert toll_charge("fire_engine", 3, True, True) == 0


def test_non_exempt_vehicle():
    assert toll_charge("car", 2, False, False) == 100


def test_pass_advice_buy_pass():
    assert pass_advice([(False, False)], 2, 90) == "buy_pass"


def test_pass_advice_either_option():
    assert pass_advice([(False, False)], 2, 100) == "either"


def test_pass_advice_pay_per_trip():
    assert pass_advice([(False, False)], 2, 110) == "pay_per_trip"


def test_pass_advice_multiple_trips():
    trips = [(False, False), (True, False)]
    assert pass_advice(trips, 2, 200) == "buy_pass"
