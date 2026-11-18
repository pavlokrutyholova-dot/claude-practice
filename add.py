"""Прості арифметичні функції."""


def add(a, b):
    """Повертає суму двох чисел."""
    return a + b


def multiply(a, b):
    """Повертає добуток двох чисел."""
    return a * b


if __name__ == "__main__":
    x = float(input("Перше число: "))
    y = float(input("Друге число: "))
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
