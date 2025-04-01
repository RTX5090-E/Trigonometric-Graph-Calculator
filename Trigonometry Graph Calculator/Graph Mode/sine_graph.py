from matplotlib import pyplot as plt
import numpy as np

def plot_sine_graph():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100000)
    plt.plot(x, np.sin(x), label='sin(x)')
    plt.legend(loc='upper right')
    plt.title('Sine Function')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.grid(True)
    plt.show()