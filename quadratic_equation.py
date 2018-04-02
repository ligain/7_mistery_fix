from math import sqrt


def get_roots(a, b, c):
    """
    Функция для нахождения корней
    квадратного уравнения вида:
    `a * x ** 2 + b * x + c`
    :param a: number
    :param b: number
    :param c: number
    :return: tuple
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return None, None

    root1 = (-b - sqrt(discriminant)) / (2 * a)

    if discriminant == 0:
        return root1, None
    else:
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
