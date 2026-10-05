import numpy as np
import matplotlib.pyplot as plt

# Semidisk: |z| < 2 en im(z) >= 0

# Parametriseer de gesloten boundary van de semi-disk (|z| <= 2, Im(z) >= 0)
# 1. Rechte basis op de reële as: z = x + 0i voor x in [-2, 2]
# 2. Cirkelvormige boog: z = 2 * e^(i*theta) voor theta in [0, pi]
theta = np.linspace(0, np.pi, 200)
arc = 2 * np.exp(1j * theta)
base = np.linspace(-2, 2, 100) + 0j

# Voeg het rechte segment en de boog samen tot één gesloten contour-array
z_boundary = np.concatenate([base, arc])

def F(z):
    return z + 1j
def G(z):
    return np.exp(np.pi*0.25 *1j) * z
def H(z):
    return z/2



def plot_semi_disk(z_bound, title):
    plt.figure(figsize=(8, 8))
    
    # Visualiseer de originele semi-disk als gevuld gebied en gesloten boundary
    plt.fill(np.real(z_bound), np.imag(z_bound), color='blue', alpha=0.2, label='Originele semi-disk')
    plt.plot(np.real(z_bound), np.imag(z_bound), color='blue', lw=1.5)
    
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

#plot_semi_disk(z_boundary, 'Originele semi-disk: |z| < 2 en Im(z) >= 0')
#plot_semi_disk(G(F(z_boundary)), rf'Transformatie G o F:  $z \to e^{{(\pi/4  i)}}  (z + i)$')
plot_semi_disk(G(H(z_boundary)), rf'Transformatie G o H:  $z \to e^{{(\pi/4  i)}}  (z/2)$')