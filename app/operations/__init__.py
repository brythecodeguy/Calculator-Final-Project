from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(a: Number, b: Number) -> Number:
    return a ** b


def modulus(a: Number, b: Number) -> Number:
    if b == 0:
        raise ValueError("Cannot calculate modulus by zero!")
    return a % b


OPERATIONS = {
    "addition": add,
    "subtraction": subtract,
    "multiplication": multiply,
    "division": divide,
    "power": power,
    "modulus": modulus,
}


def calculate(operation_type: str, a: Number, b: Number) -> Number:
    operation = OPERATIONS.get(operation_type.lower())
    if not operation:
        raise ValueError(f"Unsupported calculation type: {operation_type}")
    return operation(a, b)
