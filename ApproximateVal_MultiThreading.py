import time
import threading


def Trapezoidal_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = f(a) + f(b)
    for i in range(1, n):
        sum_val += 2 * f(a + i * h)
    print("Integration using Trapezoidal_Rule in multiThreading is: ", (h / 2) * sum_val)


def Simpsons_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = f(a)+f(b)
    for i in range(1, n, 2):
        sum_val += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        sum_val += 2 * f(a + i * h)
    print("Integration using Simpsons_Rule in multiProcessing is: ", (h / 3) * sum_val)


# get mathematical function
user_input = input('Enter a Function : ').strip()
f = eval(f"lambda x: {user_input}")

a = float(input('Enter the value of x0 : '))
b = float(input('Enter the value of xn : '))
n = int(input('Enter the number of sub_intervals : '))
# Making sure the number of divisions is even.
while n % 2:
    print("You entered odd number. Please enter an even number")
    n = int(input('Please enter an even number : '))

start = time.time()

t1 = threading.Thread(target=Trapezoidal_Rule, args=(f, a, b, n))
t2 = threading.Thread(target=Simpsons_Rule, args=(f, a, b, n))

t1.start()
t2.start()
t1.join()
t2.join()

print("Time taken is: ", time.time() - start)
