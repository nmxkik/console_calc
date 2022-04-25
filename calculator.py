from calc import Calc
from constants import *


def main(*expression):
    """Main loop: Read and calculate user's input."""
    print(WELCOME)
    while True:
        # Read user's input
        try:
            expression = input(">>> ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Handle special commands
        if expression.lower() == "help":
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()

        # calculate the expression and handle errors
        c = Calc(expression)
        try:
            result = c.calculate(expression)
        except SyntaxError:
            # If the user enters an invalid expression
            print("Invalid input expression syntax")
            continue
        except (NameError, ValueError) as err:
            # If the user tries to use a name that isn't allowed
            # or an invalid value to a given math function
            print(err)
            continue

        # Print the result if no error occurs
        print(f"The result is: {result}")


if __name__ == "__main__":
    main()
