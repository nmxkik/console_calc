from calc import Calc
from constants import ALLOWED_NAMES, USAGE, WELCOME
from calculation_history import History


def clear_сonsole():
    print('\n' * 150)


def main():
    c = Calc()
    clear_сonsole()
    print(WELCOME)
    History.create_calculation_history_csv_with_headers()
    while True:
        try:
            expression = input("Enter a math expression: ")
        except (KeyboardInterrupt, EOFError):
            raise SystemExit()
        if expression.lower() == "help":
            clear_сonsole()
            print(USAGE)
            continue
        elif expression.lower() in ["quit", "exit"]:
            raise SystemExit()
        elif expression.lower() == "history":
            clear_сonsole()
            History.get_calculation_history()
            continue
        elif expression.lower() == "clear":
            History.create_calculation_history_csv_with_headers()
            clear_сonsole()
            print("History has been deleted")
            continue
        try:
            result = c.calculate(expression)
            row_to_write = [History.get_nomber_of_lines(), expression, result]
            History.write_line_in_calculation_history_csv(row_to_write)
        except SyntaxError:
            clear_сonsole()
            print(WELCOME)
            print("Invalid input expression syntax")
            continue
        except ZeroDivisionError:
            clear_сonsole()
            print(WELCOME)
            print("Can`t divide by zero!")
            continue
        except (NameError, ValueError) as err:
            print(err)
            continue
        clear_сonsole()
        print(WELCOME)
        print(f"The result is: {expression} = {result}")


if __name__ == "__main__":
    main()
