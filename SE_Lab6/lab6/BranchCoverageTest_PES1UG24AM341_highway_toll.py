
import pytest

from highway_toll import toll_for, toll_charge, pass_advice


@pytest.mark.parametrize("axles", [0, 1])
def test_invalid_axle_counts(axles):
    with pytest.raises(ValueError, match="invalid axle count"):
        toll_for(axles, False, False)


@pytest.mark.parametrize(
    "axles, expected",
    [(2, 100), (3, 150), (4, 250), (5, 400)],
)
def test_base_toll_branches(axles, expected):
    assert toll_for(axles, False, False) == expected


@pytest.mark.parametrize(
    "axles, is_peak, has_fastag, expected",
    [
        (2, False, False, 100),
        (2, True, False, 125),
        (2, False, True, 90),
        (2, True, True, 112.5),
        (3, False, True, 142.5),
        (4, True, True, 296.88),
        (5, True, False, 500),
        (5, False, True, 380),
    ],
)
def test_toll_calculation_branches(axles, is_peak, has_fastag, expected):
    assert toll_for(axles, is_peak, has_fastag) == expected


@pytest.mark.parametrize("vehicle", ["ambulance", "fire_engine"])
def test_exempt_vehicle_branches(vehicle):
    assert toll_charge(vehicle, 2, False, False) == 0


def test_non_exempt_vehicle_branch():
    assert toll_charge("car", 3, False, False) == 150


@pytest.mark.parametrize(
    "trips, pass_price, expected",
    [
        ([(False, False)], 90, "buy_pass"),
        ([(False, False)], 100, "either"),
        ([(False, False)], 110, "pay_per_trip"),
        ([], 100, "pay_per_trip"),
        ([(False, False), (True, False)], 200, "buy_pass"),
    ],
)
def test_pass_advice_branches(trips, pass_price, expected):
    assert pass_advice(trips, 2, pass_price) == expected
