import os
import pathlib
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")
matplotlib.use("Agg")

output_dir = (
    pathlib.Path(__file__).resolve().parent.parent.parent
    / "Moeilijkheden"
    / "figuren-voor-oef"
)
output_dir.mkdir(parents=True, exist_ok=True)


# Definiëren van de hoofdcontour |z| = 3 en kleine contouren voor deformatie
theta = np.linspace(0, 2 * np.pi, 100)
z_contour = 3 * np.exp(1j * theta)
z_small_1 = 1j + 0.4 * np.exp(1j * theta)
z_small_2 = -1j + 0.4 * np.exp(1j * theta)

plt.figure(figsize=(6, 6))

# Plotten van de hoofdcontour en de gefragmenteerde paden rond de poles
plt.plot(z_contour.real, z_contour.imag, label=r"$\Gamma^*: |z|=3$", color="blue")
plt.plot(0, 1, "ro", label="Pole $z_1 = i$ (order 2)")
plt.plot(0, -1, "ro", label="Pole $z_2 = -i$ (order 2)")
plt.plot(z_small_1.real, z_small_1.imag, "g--", label="Deformed sub-contours")
plt.plot(z_small_2.real, z_small_2.imag, "g--")

plt.axhline(0, color="black", lw=0.5)
plt.axvline(0, color="black", lw=0.5)
plt.grid(True, linestyle=":")
plt.legend()
plt.title("Contour Deformation Visualization")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.axis("equal")

# Opslaan in relatieve output path
plt.savefig(output_dir / "H4-4.5-oef4.pdf", bbox_inches="tight")
plt.close()
