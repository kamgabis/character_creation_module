from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления ' \
          'квадратного корня из заданного числа'
print(message)


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    return sqrt(Number)


def calc(your_number):
    """Вычисляет квадратный корень
    из введённого вами числа."""
    if your_number <= 0:
        return
    print(f"Мы вычислили квадратный корень из введённого"
          f'вами числа. Это будет: '
          f'{CalculateSquareRoot(your_number)}')


print(message)
calc(25.5)
