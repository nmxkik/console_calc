import math

ALLOWED_NAMES = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}

WELCOME = f"""
Enter a valid math expression after the prompt ">>>".
Type "help" for more information.
Type "quit" or "exit" to exit.
"""

USAGE = f"""
Usage:
Build math expressions using numeric values and operators.
Use any of the following functions and constants:
{', '.join(ALLOWED_NAMES.keys())}
"""
