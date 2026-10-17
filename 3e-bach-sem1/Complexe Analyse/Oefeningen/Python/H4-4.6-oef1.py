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
t = np.linspace(0, 2*np.pi, 300)
R, T = np.meshgrid(r, t)

# transformatie naar cartesische coördinaten voor een correcte ruimtelijke schijfprojectie
X = R * np.cos(T)
Y = R * np.sin(T)
Z_complex = X + 1j * Y

F = np.abs(Z_complex**2 + 3*Z_complex - 1)

# we bepalen de 2D-indexwaarde van het numerieke maximum binnen de berekende mesh
max_idx = np.unravel_index(np.argmax(F, axis=None), F.shape)
z_max_num = np.round(Z_complex[max_idx], 4)
f_max_num = F[max_idx]

print(f"Numeriek maximum van |z^2 + 3z - 1|: {f_max_num:.4f} (Theoretisch: {np.sqrt(13):.4f})")
print(f"Bereikt bij benadering op z = {z_max_num}")

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# X en Y in plaats van T en R als basisassen, met Z als magnitude
ax.plot_surface(X, Y, F, cmap='viridis', alpha=0.8)
ax.set_xlabel('Re(z)')
ax.set_ylabel('Im(z)')
ax.set_zlabel(r'$|z^2 + 3z - 1|$')
plt.title(r'3D plot of $|z^2 + 3z - 1|$ op $|z| \leq 1$')

plt.savefig(output_dir / "H4-4.6-oef1.pdf", bbox_inches='tight')
plt.close()