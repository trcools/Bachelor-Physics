import numpy as np
import matplotlib.pyplot as plt

def R(z):
    numerator = 3*(z+2)
    denominator = (z-1j)**2 * (z + 1j)
    return numerator / denominator

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
xlim = (-5, 5)
ylim = (-5, 5)

# Plot the complex function R(z)
plot_complex_function(R, xlim, ylim, title= r'$\frac{3(z+2)}{(z-i)^2(z+i)}$')