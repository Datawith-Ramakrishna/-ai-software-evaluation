"""Reference implementation for checking the evaluation pipeline.
IMPORTANT: replace with your OWN unaided implementation for a real baseline.
"""
def calculate(a: float, b: float, operation: str) -> float:
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operation")
