# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminant_val = b ** 2 - (4 * a * c)
    if discriminant_val < 0:
        return "( )"

    discriminant = discriminant_val ** 0.5
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    return (max(x1, x2), min(x1, x2))


def value_y(a, b, c, x):
    y = a * (x ** 2) + b * x + c
    return y


def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}"


def derivation(a, b, c):
    derivada_a = 2 * a
    derivada_b = b
    if derivada_a == 0 and derivada_b == 0:
        return "f'(x) = 0"
    if derivada_a == 0:
        return f"f'(x) = {derivada_b}"
    if derivada_b == 0:
        return f"f'(x) = {derivada_a} * X"
    return f"f'(x) = {derivada_a} * X + {derivada_b}"
