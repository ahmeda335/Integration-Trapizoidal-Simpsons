import time
import multiprocessing


def Trapezoidal_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = func(a, f) + func(b, f)
    for i in range(1, n):
        sum_val += 2 * func(a + i * h, f)
    print((h / 2) * sum_val)


def Simpsons_Rule(f, a, b, n):
    h = (b - a) / n
    sum_val = func(a, f)+func(b, f)
    for i in range(1, n, 2):
        sum_val += 4 * func(a + i * h, f)
    for i in range(2, n-1, 2):
        sum_val += 2 * func(a + i * h, f)
    print((h / 3) * sum_val)


def func(x, equation_string):
    # Evaluate the equation using eval() within the function
    return eval(equation_string.replace('x', str(x)))

if __name__ == '__main__':

    # get mathematical function
    user_input = str(input('Enter a Function : ')).strip()

    a = multiprocessing.Value('d', 0)
    b = multiprocessing.Value('d', 0)
    n = multiprocessing.Value('i', 0)

    a.value = float(input('Enter the value of x0 : '))
    b.value = float(input('Enter the value of xn : '))
    n.value = int(input('Enter the number of sub_intervals : '))
    # Making sure the number of divisions is even.
    while n.value % 2:
        print("You entered odd number. Please enter an even number")
        n = int(input('Please enter an even number : '))

    start = time.time()

    p1 = multiprocessing.Process(target=Trapezoidal_Rule, args=(user_input, a.value, b.value, n.value))
    p2 = multiprocessing.Process(target=Simpsons_Rule, args=(user_input, a.value, b.value, n.value))

    p1.start()
    p2.start()
    p1.join()
    p2.join()
    #
    print("Time taken is: ", time.time() - start)
