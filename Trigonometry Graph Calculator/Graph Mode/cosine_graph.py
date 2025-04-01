from matplotlib import pyplot as plt
import numpy as np

def plot_cosine_graph():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 100000)
    plt.plot(x, np.cos(x), label='cos(x)')
    plt.legend(loc='upper right')
    plt.title('Cosine Function')
    plt.xlabel('x')
    plt.ylabel('cos(x)')
    plt.grid(True)
    plt.show()