"""
This module contains the main function for the Calculator project.
"""

from calculator.calculator_logic import Calculator


def main() -> None:
    """
    The main function of the Calculator project.
    """
    print("_" * 40, end="\n\n")
    print("Welcome to the Calculator project!\n")
    print("Operations supported by this calculator:")
    print(
        "  • Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Taking (n) root of a number",
        "Calculator memory reset",
        sep=";\n  • ",
        end=".\n",
    )
    print("_" * 40, end="\n\n")

    calculator = Calculator()
    calculator.add(10)
    calculator.subtract(5)
    calculator.reset_memory()
    calculator.add(9)
    calculator.multiply(1.5)
    calculator.divide(1.5)
    calculator.nth_root(2)

    print(calculator)
    print("_" * 40, end="\n\n")


if __name__ == "__main__":
    main()
