from calc import Calc
from constants import ALLOWED_NAMES, USAGE, WELCOME
from calculation_history import History

c = Calc()


def clearConsole(): return print('\n' * 150)


clearConsole()


def main():
    """Main loop: Read and calculate user's input."""
    print(WELCOME)
    # calculation history refresh
    History.refresh_csv_file()
    while True:
        # Read user's input
        try:
            expression = input("Enter a math expression: ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()

        # Handle special commands
        if expression.lower() == "help":
            clearConsole()
            print(USAGE)
            continue
        if expression.lower() in {"quit", "exit"}:
            raise SystemExit()
        if expression.lower() == "history":
            clearConsole()
            History.read_history_file()
            continue
        if expression.lower() == "clear":
            History.refresh_csv_file()
            clearConsole()
            print("History has been deleted")
            continue
        # calculate the expression, write to history and handle errors

        try:
            result = c.calculate(expression)
            lines = History.count_lines_in_csv()
            write_down = [lines, expression, result]
            History.write_answer_in_file(write_down)
        except SyntaxError:
            # If the user enters an invalid expression
            clearConsole()
            print("Invalid input expression syntax")
            continue
            # If the user tries to divide by zero
        except ZeroDivisionError:
            clearConsole()
            print("Can`t divide by zero!")
            continue
        except (NameError, ValueError) as err:
            # If the user tries to use a name that isn't allowed
            # or an invalid value to a given math function
            clearConsole()
            print(err)
            continue

        # Print the result if no error occurs
        clearConsole()
        print(WELCOME)
        print(f"The result is: {result}")


if __name__ == "__main__":
    main()
