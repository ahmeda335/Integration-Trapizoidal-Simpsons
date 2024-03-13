# numerical_integration.py

def Trapezoidal_Rule(f, a, b, n):
    h = (a - b) / n
    sum_val = f(a) + f(b)
    for i in range(1, n):
        sum_val += 2 * f(a + i * h)
    return (h / 2) * sum_val


def Simpsons_Rule(f, a, b, n):
    h = (a - b) / n
    sum_val = f(a)+f(b)
    for i in range(1, n, 2):
        sum_val += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        sum_val += 2 * f(a + i * h)
    return (h / 3) * sum_val
