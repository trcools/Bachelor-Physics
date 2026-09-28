import numpy as np
import matplotlib.pyplot as plt

# origineel disk: |z| < 2 en im(z) >= 0

# ==========================
# Deeloefening a
# ==========================

theta = np.linspace(0, np.pi, 200)
arc = 2 * np.exp(1j * theta)
base = np.linspace(-2, 2, 100) + 0j

# Voeg het rechte segment en de boog samen tot één gesloten contour-array
z_boundary = np.concatenate([base, arc])


c_a = 3

def f(z,c):
    return z + c

def plot_semi_disk(z_bound, c, title):
    plt.figure(figsize=(8, 8))
    
    # Visualiseer de originele semi-disk als gevuld gebied en gesloten boundary
    plt.fill(np.real(z_bound), np.imag(z_bound), color='blue', alpha=0.2, label='Originele semi-disk')
    plt.plot(np.real(z_bound), np.imag(z_bound), color='blue', lw=1.5)
    
    # Bereken de getransformeerde boundary onder f(z)
    w_bound = f(z_bound, c)
    
    # Visualiseer de getransformeerde semi-disk
    plt.fill(np.real(w_bound), np.imag(w_bound), color='orange', alpha=0.3, label='Transformed semi-disk')
    plt.plot(np.real(w_bound), np.imag(w_bound), color='orange', lw=1.5)
    
    # Assen en layout instellingen
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.xlabel('Re(z)')
    plt.ylabel('Im(z)')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_semi_disk(z_boundary, c_a, 'Deeloefening a: Transformatie van een semi-schijf')

# ==========================
# Deeloefening b
# ==========================


c_b = 2j
plot_semi_disk(z_boundary, c_b, 'Deeloefening b: Transformatie van een semi-schijf')

# ==========================
# Deeloefening c
# ==========================

c_c = -1 - 1j
plot_semi_disk(z_boundary, c_c, 'Deeloefening c: Transformatie van een semi-schijf')
