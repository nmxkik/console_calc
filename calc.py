from constants import ALLOWED_NAMES


class Calc():

    def calculate(self, expression):
        """Evaluate a math expression."""
        # Compile the expression eventually raising a SyntaxError
        # when the user enters an invalid expression
        code = compile(expression, "<string>", "eval")

        # Validate allowed names
        for name in code.co_names:
            if name not in ALLOWED_NAMES:
                raise NameError(f"The use of '{name}' is not allowed")

        # Evaluate the expression eventually raising a ValueError
        # when the user uses a math function with a wrong input value
        # e.g. math.sqrt(-10)
        return eval(code, {"__builtins__": {}}, ALLOWED_NAMES)
