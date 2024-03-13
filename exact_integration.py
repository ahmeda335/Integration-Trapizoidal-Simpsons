import sympy as sp


def evaluate_integral(expression, a, b):
    try:
        # Convert the input string into a symbolic expression
        x = sp.symbols('x')
        integrand = sp.sympify(expression)

        # Evaluate the integral
        result = sp.integrate(integrand, (x, a, b))
        return result  # Return the result of the integration
    except (sp.SympifyError, ValueError):
        return None  # Return None if there's an error in input or integration

