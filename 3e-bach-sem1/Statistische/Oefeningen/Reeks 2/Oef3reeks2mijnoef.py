import numpy as np
import matplotlib.pyplot as plt

var = np.linspace(-25, 25, 10000)


def c_v_kt(var):
    return (var / (np.exp(var) + 1)) ** 2 * np.exp(var)


plt.plot(var, c_v_kt(var))
plt.xlabel(r"($\beta \epsilon$)")
plt.ylabel(r"$\frac{C_v}{Nk}$")
plt.title(r"Heat Capacity: $\frac{C_v}{Nk}$ in function of $\beta \epsilon$")
plt.show()
