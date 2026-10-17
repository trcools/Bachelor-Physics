import os
import pathlib
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")
matplotlib.use("Agg")

output_dir = pathlib.Path(__file__).resolve().parent.parent.parent / "Moeilijkheden" / "figuren-voor-oef"
output_dir.mkdir(parents=True, exist_ok=True)

# meshgrid is vereist voor het 2D opspannen van de volledige schijf
r = np.linspace(0, 1, 300)
theta = np.linspace(0, 5*np.pi, 300)
R, Theta = np.meshgrid(r, theta)

# transformatie naar cartesische coördinaten voor een correcte ruimtelijke schijfprojectie
X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = X + 1j * Y

F = np.log(np.abs(Z))+1j*np.angle(Z)

# plot imagonair deel

fig = plt.figure(figsize=(16, 8))

# Eerste subplot: Cartesiaanse projectie (X, Y)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot_surface(X, Y, np.imag(F), cmap='viridis', alpha=0.8)
ax1.set_xlabel('Re(z)')
ax1.set_ylabel('Im(z)')
ax1.set_zlabel('Im(f(z))')
ax1.set_title(r'Imaginary part of $f(z) = \log(z)$ (Cartesian)')

# Tweede subplot: Polaire projectie (R, Theta)
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
ax2.plot_surface(R, Theta, np.imag(F), cmap='viridis', alpha=0.8)
ax2.set_xlabel('r')
ax2.set_ylabel('θ')
ax2.set_zlabel('Im(f(z))')
ax2.set_title(r'Imaginary part of $f(z) = \log(z)$ (Polar)')


plt.savefig(output_dir / "H4-4.6-oef2.pdf", bbox_inches='tight')
plt.close()