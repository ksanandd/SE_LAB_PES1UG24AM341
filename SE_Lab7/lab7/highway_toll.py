
def parse_plate(plate):
    # Validate input type
    if not isinstance(plate, str):
        return None

    parts = plate.strip().split('-')

    # Validate the number of components
    if len(parts) != 4:
        return None

    state, district, series, number = parts

    # Validate individual plate components
    if not (len(state) == 2 and state.isalpha()):
        return None

    if not (len(district) == 2 and district.isdigit()):
        return None

    if not (1 <= len(series) <= 3 and series.isalpha()):
        return None

    if not (1 <= len(number) <= 4 and number.isdigit()):
        return None

    return state.upper(), int(district), int(number)


def trip_cost(text):
    # Validate input type
    if not isinstance(text, str):
        return None

    text = text.strip().lower()

    # Ensure exactly one separator exists
    if text.count('x') != 1:
        return None

    count, rate = text.split('x')

    # Validate numeric values
    if not count.strip().isdigit() or not rate.strip().isdigit():
        return None

    return int(count.strip()) * int(rate.strip())


def axle_class(axles):
    # Validate input type
    if not isinstance(axles, (str, int)) or isinstance(axles, bool):
        return None

    try:
        n = int(axles)
    except (ValueError, TypeError):
        return None

    # Reject invalid axle counts
    if n < 2:
        return None

    if n == 2:
        return 'car'
    if n <= 4:
        return 'truck'
    return 'heavy'


def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result)

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result)

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result)


if __name__ == "__main__":
    main()
