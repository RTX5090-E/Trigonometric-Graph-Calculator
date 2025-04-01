from matplotlib import pyplot as plt
import numpy as np

def plot_tangent_graph():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100000)
    plt.plot(x, np.tan(x), label='tan(x)')
    plt.legend(loc='upper right')
    plt.title('Tangent Function')
    plt.xlabel('x')
    plt.ylabel('tan(x)')
    plt.grid(True)
    plt.show()