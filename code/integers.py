def validate_odd_positive_integer(number: int):
    """
    Validates that the input is an odd, positive integer.

    Args:
        number (int): The number to validate.

    Raises:
        ValueError: If the input is not an integer, not positive, or not odd.
    """
    eval(number)
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    if number <= 0:
        raise ValueError("Number must be positive")
    if number % 2 == 0:
        raise ValueError("Number must be odd")


def validate_even_negative_integer(number: int):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    if number >= 0:
        raise ValueError("Number must be negative")
    if number % 2 != 0:
        raise ValueError("Number must be even")



