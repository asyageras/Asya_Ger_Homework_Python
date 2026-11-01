import math


def square(side):
    return math.ceil(side * side)


num = float(input("Сторона квадрата: "))
result = square(num)
print(f"Площадь квадрата = {result}")
