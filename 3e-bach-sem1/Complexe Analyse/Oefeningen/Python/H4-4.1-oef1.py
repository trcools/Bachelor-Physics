import os
import pathlib
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")
matplotlib.use("Agg")  # Non-interactive backend for generating files

# Pad naar de doelmap
output_dir = (
    pathlib.Path(__file__).resolve().parent.parent.parent
    / "Moeilijkheden"
    / "figuren-voor-oef"
)
output_dir.mkdir(parents=True, exist_ok=True)
print(f"Output directory: {output_dir}")

t = np.linspace(0, 2 * np.pi, 100)

# conditie: |z-2i| = 4, startend van z=4+2i
z = 4 + 2j
c = 2j
r = 4
z_circle = c + r * np.exp(1j * t)

plt.plot(z_circle.real, z_circle.imag, "b-", label="|z-2i| = 4")
plt.plot(z.real, z.imag, "ro", label="Startpunt z=4+2i")
plt.axis("equal")
plt.grid(True)
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Cirkel |z-2i| = 4")

plt.savefig(output_dir / "H4-4.1-oef1(b).pdf", bbox_inches="tight")
plt.close()
print("Saved H4-4.1-oef1(b).pdf")
