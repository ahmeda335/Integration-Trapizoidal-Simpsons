# main.py
from numerical_integration import Trapezoidal_Rule, Simpsons_Rule
import exact_integration
import Plotting

# Use functions from numerical_integration.py

user_input = input('Enter your Function : ')
f = eval(f"lambda x: {user_input}")

a = float(input('Enter the lower limit of integration: '))
b = float(input('Enter the upper limit of integration: '))
n = int(input('Enter the number of sub_intervals : '))
h = (a - b) / n
while n % 2:
    print("You entered odd number. Please enter an even number")
    n = int(input('Please enter an even number : '))


# ------------------------- Printing exact Result --------------------------- #
print('-'*80)
exact_result = exact_integration.evaluate_integral(user_input, a, b)
if exact_result is not None:
  print("Exact value of the integral:", exact_result)
else:
    print("Unable to evaluate the integral.")


# ----------------- Printing Approximate Result --------------------------- #
Integration_Trapezoidal_Rule = abs(float(Trapezoidal_Rule(f, a, b, n)))
Integration_Simpsons_Rule = abs(float(Simpsons_Rule(f, a, b, n)))
print('-'*80)
print('The Approximate Integration using Trapezoidal Rule', Integration_Trapezoidal_Rule)
print('The Approximate Integration using Simpsons Rule', Integration_Simpsons_Rule)


# ----------------------- Printing Errors ---------------------------------- #
# Use integration_result  from exact_integration.py to know absolute_error
print('-'*80)
print('The Absolute Error of Integration using Trapezoidal Rule = ', Integration_Trapezoidal_Rule - exact_result )
print('The Absolute Ealue of Integration using Simpsons Rule = ', Integration_Simpsons_Rule - exact_result )

# Use integration_result  from exact_integration.py to know relative_error
print('-'*80)
print(f'The Relative Error of Integration using Trapezoidal Rule = {((Integration_Trapezoidal_Rule - exact_result)/exact_result)*100} % ')
print(f'The Relative Error of Integration using Simpsons Rule = {((Integration_Simpsons_Rule - exact_result)/exact_result)*100} % ')
print('-'*80)

# --------------------------- Plotting --------------------------------- #
Plotting.draw_input_func(user_input, a, b, n)
