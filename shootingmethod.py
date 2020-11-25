import math
from scipy.misc import derivative

VAR = 20

EPS = 1e-4

EPS1 = 1e-5


def A(x):
    if VAR == 20: return 30 * (-x + 0.5)
    elif VAR == 24: return 40 * (-x + 0.5)
    else: return 0


def B(x):
    if VAR == 20: return x ** 2 + 2
    elif VAR == 24: return -(x ** 2) + 2
    else: return 0


def C(x):
    if VAR == 20 or VAR == 24: return x + 2
    else: return 0


# Yпр(x)
def Ynp(x):
    return 1 + x + 10 * math.log(VAR + 1) * x ** 3 * (1 - x) ** 3

# Краевая задача
def F(x):
    d2Ynp = derivative(Ynp, x, dx=1e-5, n=2)
    dYnp = derivative(Ynp, x, dx=1e-5)
    return d2Ynp + A(x) * dYnp - B(x) * Ynp(x) + C(x) * math.sin(Ynp(x))


#
def f(x, y, z):
    return -A(x) * z + B(x) * y - C(x) * math.sin(y) + F(x)

# Автоматический выбор шага
def calculate_h(x, y, z, h):
    k1 = h * z
    l1 = h * f(x, y, z)
    k2 = h * (z + l1 / 2)
    l2 = h * f(x + h / 2, y + k1 / 2, z + l1 / 2)
    k3 = h * (z + l2 / 2)
    l3 = h * f(x + h / 2, y + k2 / 2, z + l2 / 2)
    k4 = h * (z + l3)
    l4 = h * f(x + h, y + k3, z + l3)
    return (y + (k1 + 2 * k2 + 2 * k3 + k4) / 6,
            z + (l1 + 2 * l2 + 2 * l3 + l4) / 6)

# метод Рунге-Кутты
def runge_kutta_method(alpha, xPar, delta, toprint=False):
    x, y, z = 0, 1, alpha  # x=0, y(0)=1, y'(0)=alpha
    yPrev, zPrev = 0, 0

    delta[0] = 0

    if toprint:
        print(f'{"x":9}|\t{"y(x)":9}|\t{"Ypr(x)":9}|\t{"z(x)":9}|\t{"Delta":12}|')

    while x < xPar:
        y1, y2, y3, z1 = 1, 0, 0, 0
        h = 0.1
        while abs(y1 - y3) > EPS1:
            yPrev, zPrev, z1 = y, z, z

            y1, z1 = calculate_h(x, yPrev, z1, h)
            y2, zPrev = calculate_h(x, yPrev, zPrev, h / 2)
            y3, zPrev = calculate_h(x, y2, zPrev, h / 2)

            h /= 2

        Y = Ynp(x)
        error = abs(Y - y)
        delta[0] = error if error > delta[0] else delta[0]

        if toprint:
            print(f'{x:9.6f}|\t{y:9.6f}|\t{Y:9.6f}|\t{z:9.6f}|\t{error:9e}|')

        yPrev = y

        y, z = calculate_h(x, y, z, h)

        x += h
    return yPrev


def shootingmethod():
    print('Метод стрельб\n')

    alpha1, alpha2, alpha, delta, y = 0, 3, 0, [0], 0
    B, itr = 2, 0

    print(f'{"Itr":9}|\t{"z(0)":9}|\t{"y(1)":9}|\t{"Delta":12}|')

    while abs(y - B) > EPS:
        itr += 1
        alpha = (alpha1 + alpha2) / 2
        y = runge_kutta_method(alpha, 1, delta)

        if y > B:
            alpha2 = alpha
        else:
            alpha1 = alpha

        print(f'{itr:9d}|\t{alpha:9.6f}|\t{y:9.6f}|\t{delta[0]:9e}|')

    print()
    runge_kutta_method(alpha, 1, delta, toprint=True)
