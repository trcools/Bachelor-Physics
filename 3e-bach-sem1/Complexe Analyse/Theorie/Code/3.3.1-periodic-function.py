import numpy as np
import matplotlib.pyplot as plt

def R(z):
    return np.exp(z)

def plot_complex_function(func, xlim, ylim, num_points=1000, title='Complex Function Plot'):
    x = np.linspace(xlim[0], xlim[1], num_points)
    y = np.linspace(ylim[0], ylim[1], num_points)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    W = func(Z)

    plt.figure(figsize=(10, 8))
    plt.imshow(np.angle(W), extent=(xlim[0], xlim[1], ylim[0], ylim[1]), origin='lower', cmap='Blues')
    plt.colorbar(label='Argument (angle)')
    plt.title(rf'Argument of the complex function $ R(z) =$' + title )
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.grid()
    plt.show()

# Define the limits for the plot
xlim = (-25, 25)
ylim = (-25, 25)

# Plot the complex function R(z)
plot_complex_function(R, xlim, ylim, title= r'$\exp(z)$')