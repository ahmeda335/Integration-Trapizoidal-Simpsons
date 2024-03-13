import matplotlib.pyplot as plt
import numpy as np
from exact_integration import evaluate_integral


def draw_input_func(user_input, a, b, n):
    h = (b - a) / n
    f = eval(f"lambda x: {user_input}")
    x_values = np.arange(a, b, h)
    # Plot the expression
    fig, ax = plt.subplots()
    ax.plot(x_values, f(x_values), color='blue', alpha=1.00)
    ax.fill_between(x_values, f(x_values), 0, color='blue', alpha=.1)
    plt.title('Plot of ' + user_input)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


def draw_output_func(integral, a, b, n):
    user_input = eval(f"lambda x: {evaluate_integral}")
    # print(user_input)
    # print(user_input(2))
    h = (b - a) / n
    x_values = np.arange(a, b, h)
    # Plot the expression
    fig, ax = plt.subplots()
    ax.plot(x_values, user_input(x_values), color='blue', alpha=1.00)
    ax.fill_between(x_values, user_input(x_values), 0, color='blue', alpha=.1)
    plt.title('Plot of ' + f"{integral}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


def draw_input_output_funcs(user_input, integral, a, b, n):

    user_input_eval = eval(f"lambda x: {user_input}")

    integral_eval = eval(f"lambda x: {integral}")

    h = (b - a) / n
    x_values = np.arange(a, b, h)

    # Plot the expression
    fig, ax = plt.subplots(1, 2, figsize=(12,3), sharey=True)

    # Input Graph
    ax[0].plot(x_values, user_input_eval(x_values), color='blue', alpha=1.00)
    ax[0].fill_between(x_values, user_input_eval(x_values), 0, color='blue', alpha=.1)
    ax[0].set_title('Plot of ' + f"{user_input}")

    # Output Graph
    ax[1].plot(x_values, integral_eval(x_values), color='red', alpha=1.00)
    ax[1].fill_between(x_values, integral_eval(x_values), 0, color='red', alpha=.1)
    ax[1].set_title('Plot of ' + f"{integral}")


    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.show()


# # function before integration
# user_input = expression
#
# # function after integration -->> integral
# draw_input_output_funcs(user_input, integral, a, b, n)
