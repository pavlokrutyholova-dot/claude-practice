"""A program that adds two numbers."""

from decimal import Decimal, InvalidOperation, localcontext

# Largest allowed order of magnitude (10**MAX_EXPONENT).
MAX_EXPONENT = 100
# Enough precision for the sum of any two allowed numbers to be exact.
PRECISION = 2 * MAX_EXPONENT + 50


def add(a: Decimal, b: Decimal) -> Decimal:
    with localcontext(prec=PRECISION):
        return a + b


def parse_number(text: str) -> Decimal:
    """Convert text to a number. The decimal separator can be a comma or a dot.

    Raises ValueError with an explanation if the text is not a valid number.
    """
    text = text.strip()
    if not text:
        raise ValueError("You didn't enter anything.")
    if "_" in text:
        raise ValueError("Write the number without underscores.")
    if "," in text and "." in text:
        raise ValueError("Use either a comma or a dot, not both.")
    text = text.replace(",", ".")
    try:
        value = Decimal(text)
    except InvalidOperation:
        raise ValueError("That's not a number.") from None
    if not value.is_finite():
        raise ValueError("Please enter a regular finite number.")
    if value and abs(value.adjusted()) > MAX_EXPONENT:
        raise ValueError("The number is too large or too small.")
    return value


def format_number(value: Decimal) -> str:
    """Format a number in plain notation, without an exponent or trailing zeros."""
    text = f"{value:f}"
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return "0" if text in ("-0", "") else text


def read_number(prompt: str) -> Decimal:
    while True:
        try:
            return parse_number(input(prompt))
        except ValueError as error:
            print(f"{error} Try again.")


def main() -> int:
    print("Adding two numbers. Use a comma or a dot for decimals (for example, 2.5).")
    try:
        x = read_number("First number: ")
        y = read_number("Second number: ")
    except EOFError:
        print("\nInput interrupted.")
        return 1
    except KeyboardInterrupt:
        print("\nCancelled.")
        return 130
    print(f"Sum: {format_number(add(x, y))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
