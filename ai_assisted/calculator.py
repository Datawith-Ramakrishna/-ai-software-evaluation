"""Reference implementation for checking the evaluation pipeline.
IMPORTANT: replace with code actually created WITH AI for a real experiment.
"""
from operator import add, sub, mul, truediv

_OPERATIONS = {"add": add, "subtract": sub, "multiply": mul, "divide": truediv}

def calculate(a: float, b: float, operation: str) -> float:
    if operation not in _OPERATIONS:
        raise ValueError("Unsupported operation")
    if operation == "divide" and b == 0:
        raise ValueError("Cannot divide by zero")
    return _OPERATIONS[operation](a, b)
