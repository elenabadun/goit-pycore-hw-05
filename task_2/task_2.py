import re
from typing import Callable


def generator_numbers(text: str):
    """The function finds all real numbers in a given string and generates them, returning numbers."""
    pattern = r"\d+\.\d+"
    numbers = re.findall(pattern, text)
    for num in numbers:
        yield float(num)
        print(float(num))


def sum_profit(text: str, func: Callable):
    """The function takes two parameters: string and 'Callable' function and return sum of numbers."""
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
