import numpy as np
import matplotlib.pyplot as plt
import cmath


r = 1
t = np.linspace(0, 2 * np.pi, 100)

# ==========================
# Deeloefening a
# ==========================

def theta_a(t):
    # theta(t) = (1-i)*t
    return (1 - 1j) * t

z_a = r * np.exp(1j * theta_a(t))

# ==========================
# Deeloefening b
# ==========================


def theta_b(t):
    # theta(t) = -(1+i)*t
    return -(1 + 1j) * t

z_b = r * np.exp(1j * theta_b(t))

# ==========================
# Deeloefening c
# ==========================

def theta_c(t):
    # theta(t) = (1+i)*t
    return (1 + 1j) * t
z_c = r * np.exp(1j * theta_c(t))


# ==========================
# Deeloefening d
# ==========================

def theta_d(t):
    # theta(t) = (i-1)*t
    return (1j-1) * t
z_d = r * np.exp(1j * theta_d(t))


def plot_complex_function(z):
    plt.figure(figsize=(6, 6))
    plt.plot(z.real, z.imag)
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.title('Complex Function')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_complex_function(z_d)
