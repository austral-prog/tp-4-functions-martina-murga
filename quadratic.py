# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = (b ** 2 - (4 * a * c)) ** 0.5
    x1 = (-b + discriminante) / (2 * a)
    x2 = (-b - discriminante) / (2 * a)
    return x1, x2


def value_y(a, b, c, x):
    y = a * (x ** 2) + b * x + c
    return y


def to_string(a, b, c):
    return f"f(x) = {a}x^2 + {b}x + {c}"


def derivation(a, b, c):
    derivada_a = 2 * a
    derivada_b = b
    return f"f'(x) = {derivada_a}x + {derivada_b}"
