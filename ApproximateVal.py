import time

def Trapezoidal_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = f(a) + f(b)
    for i in range(1, n):
        sum_val += 2 * f(a + i * h)
    print((h / 2) * sum_val)


def Simpsons_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = f(a)+f(b)
    for i in range(1, n, 2):
        sum_val += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        sum_val += 2 * f(a + i * h)
    print((h / 3) * sum_val)


# get mathematical function
user_input = input('Enter a Function : ').strip()
f = eval(f"lambda x: {user_input}")

a = float(input('Enter the value of x0 : '))
b = float(input('Enter the value of xn : '))
n = int(input('Enter the number of sub_intervals : '))

while n % 2:
    print("You entered odd number. Please enter an even number")
    n = int(input('Please enter an even number : '))

start = time.time()
# Integration_Trapezoidal_Rule = Trapezoidal_Rule(f, a, b, n)
# Integration_Simpsons_Rule = Simpsons_Rule(f, a, b, n)

print('The Approximate value of Integration using Trapezoidal Rule', Trapezoidal_Rule(f, a, b, n))
print('The Approximate value of Integration using Simpsons Rule', Simpsons_Rule(f, a, b, n))

print("Time taken is: ", time.time() - start)
