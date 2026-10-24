import os
import pathlib
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Systeemconfiguratie en output_dir setup behouden
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")
matplotlib.use("Agg")
output_dir = (
    pathlib.Path(__file__).resolve().parent.parent.parent
    / "Figuren"
    / "figuren-theorie"
)
output_dir.mkdir(parents=True, exist_ok=True)


def plot_phase_complex():
    # Visualisatie 1: Phase map (hoek) van de complexe functies
    # Genereer het complex plane array
    x, y = np.linspace(-4, 4, 400), np.linspace(-4, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Definieer de 4 trig-functies
    tanZ = np.tan(Z)
    cotZ = 1 / tanZ
    secZ = 1 / np.cos(Z)
    cosecZ = 1 / np.sin(Z)

    fig, axs = plt.subplots(2, 2, figsize=(10, 8))

    # Gebruik cmap="hsv" om de cyclische phase correct te modelleren
    axs[0, 0].imshow(
        np.angle(tanZ), extent=(-4, 4, -4, 4), origin="lower", cmap="Blues"
    )
    axs[0, 0].set_title("Phase: tan(z)")

    axs[0, 1].imshow(
        np.angle(cotZ), extent=(-4, 4, -4, 4), origin="lower", cmap="Blues"
    )
    axs[0, 1].set_title("Phase: cot(z)")

    axs[1, 0].imshow(
        np.angle(secZ), extent=(-4, 4, -4, 4), origin="lower", cmap="Blues"
    )
    axs[1, 0].set_title("Phase: sec(z)")

    axs[1, 1].imshow(
        np.angle(cosecZ), extent=(-4, 4, -4, 4), origin="lower", cmap="Blues"
    )
    axs[1, 1].set_title("Phase: cosec(z)")

    plt.tight_layout()
    plt.savefig(output_dir / "complex_phase_trig.pdf", bbox_inches="tight")
    plt.close()


def plot_magnitude_complex():
    # Visualisatie 2: Magnitude map (amplitude) om polen en nulpunten te zien
    # Syntaxis voor broadcasting naar een 2D complex array
    z = np.linspace(-4, 4, 400) + 1j * np.linspace(-4, 4, 400)[:, np.newaxis]

    tan_z = np.tan(z)
    cot_z = 1 / tan_z
    sec_z = 1 / np.cos(z)
    cosec_z = 1 / np.sin(z)

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))

    # Gebruik np.abs() voor magnitude.
    # vmax=5 dient als boundary condition/clipping randvoorwaarde rond de polen (oneindig)
    axs[0, 0].imshow(
        np.abs(tan_z), extent=(-4, 4, -4, 4), origin="lower", cmap="viridis", vmax=5
    )
    axs[0, 0].set_title("Magnitude: tan(z)")

    axs[0, 1].imshow(
        np.abs(cot_z), extent=(-4, 4, -4, 4), origin="lower", cmap="viridis", vmax=5
    )
    axs[0, 1].set_title("Magnitude: cot(z)")

    axs[1, 0].imshow(
        np.abs(sec_z), extent=(-4, 4, -4, 4), origin="lower", cmap="viridis", vmax=5
    )
    axs[1, 0].set_title("Magnitude: sec(z)")

    axs[1, 1].imshow(
        np.abs(cosec_z), extent=(-4, 4, -4, 4), origin="lower", cmap="viridis", vmax=5
    )
    im4 = axs[1, 1].set_title("Magnitude: cosec(z)")

    cbar_ax = fig.add_axes([0.90, 0.25, 0.03, 0.5])

    fig.colorbar(im4, cax=cbar_ax, label="Magnitude", shrink=0.6)
    plt.tight_layout()
    plt.savefig(output_dir / "complex_magnitude_trig.pdf", bbox_inches="tight")
    plt.close()


plot_phase_complex()
plot_magnitude_complex()
