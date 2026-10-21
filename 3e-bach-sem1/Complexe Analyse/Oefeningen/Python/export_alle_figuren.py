import os
import pathlib
import numpy as np
import matplotlib

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib_cache")
matplotlib.use("Agg")  # Non-interactive backend for generating files
import matplotlib.pyplot as plt

# Pad naar de doelmap
output_dir = (
    pathlib.Path(__file__).resolve().parent.parent.parent
    / "Moeilijkheden"
    / "figuren-voor-oef"
)
output_dir.mkdir(parents=True, exist_ok=True)
print(f"Output directory: {output_dir}")

# =============================================================
# 1. H1-1.5-oef7
# =============================================================
r = 1
t = np.linspace(0, 2 * np.pi, 500)

deels = {
    "a": ((1 - 1j) * t, r"$\theta(t) = (1 - i)t$"),
    "b": (-(1 + 1j) * t, r"$\theta(t) = -(1 + i)t$"),
    "c": ((1 + 1j) * t, r"$\theta(t) = (1 + i)t$"),
    "d": ((1j - 1) * t, r"$\theta(t) = (i - 1)t$"),
}

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
for ax, (label, (theta_val, expr)) in zip(axes.flat, deels.items()):
    z = r * np.exp(1j * theta_val)
    ax.plot(z.real, z.imag, color="blue", lw=1.5)
    ax.set_title(f"Deeloefening ({label}): {expr}")
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.grid(True, linestyle="--", alpha=0.6)
    ax.set_aspect("equal")

plt.tight_layout()
plt.savefig(output_dir / "H1-1.5-oef7.pdf", bbox_inches="tight")
plt.close()
print("Saved H1-1.5-oef7.pdf")

# =============================================================
# 2. H2-1.1-oef4
# =============================================================
theta = np.linspace(0, np.pi, 300)
arc = 2 * np.exp(1j * theta)
base = np.linspace(-2, 2, 100) + 0j
z_boundary = np.concatenate([base, arc])


def plot_disk_subplot(ax, z_bound, c, title, label_trans):
    ax.fill(
        np.real(z_bound), np.imag(z_bound), color="blue", alpha=0.2, label="Origineel"
    )
    ax.plot(np.real(z_bound), np.imag(z_bound), color="blue", lw=1.2)
    w_bound = z_bound + c
    ax.fill(
        np.real(w_bound), np.imag(w_bound), color="orange", alpha=0.3, label=label_trans
    )
    ax.plot(np.real(w_bound), np.imag(w_bound), color="orange", lw=1.2)
    ax.axhline(0, color="black", lw=0.5)
    ax.axvline(0, color="black", lw=0.5)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title)
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.legend(loc="upper right", fontsize="small")
    ax.grid(True, linestyle="--", alpha=0.5)


# 1 gecombineerde figuur met de 3 transformaties naast elkaar
fig, axes = plt.subplots(1, 3, figsize=(14, 4.8))
plot_disk_subplot(axes[0], z_boundary, 3, "Deeloefening (a): $z + 3$", "$w = z + 3$")
plot_disk_subplot(axes[1], z_boundary, 2j, "Deeloefening (b): $z + 2i$", "$w = z + 2i$")
plot_disk_subplot(
    axes[2], z_boundary, -1 - 1j, "Deeloefening (c): $z - 1 - i$", "$w = z - 1 - i$"
)
plt.tight_layout()
plt.savefig(output_dir / "H2-1.1-oef4.pdf", bbox_inches="tight")
plt.close()
print("Saved H2-1.1-oef4.pdf")


# =============================================================
# 3. H2-1.1-oef6
# =============================================================
def F(z):
    return z + 1j


def G(z):
    return np.exp(np.pi * 0.25 * 1j) * z


def H(z):
    return z / 2


fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Subplot 1: G o F
axes[0].fill(
    np.real(z_boundary), np.imag(z_boundary), color="blue", alpha=0.2, label="Origineel"
)
axes[0].plot(np.real(z_boundary), np.imag(z_boundary), color="blue", lw=1.2)
trans_GF = G(F(z_boundary))
axes[0].fill(
    np.real(trans_GF), np.imag(trans_GF), color="green", alpha=0.3, label=r"$G \circ F$"
)
axes[0].plot(np.real(trans_GF), np.imag(trans_GF), color="green", lw=1.2)
axes[0].axhline(0, color="black", lw=0.5)
axes[0].axvline(0, color="black", lw=0.5)
axes[0].set_xlim(-5, 5)
axes[0].set_ylim(-5, 5)
axes[0].set_aspect("equal", adjustable="box")
axes[0].set_title(r"$G \circ F: z \mapsto e^{i\pi/4}(z + i)$")
axes[0].set_xlabel("Re(z)")
axes[0].set_ylabel("Im(z)")
axes[0].legend(loc="upper right", fontsize="small")
axes[0].grid(True, linestyle="--", alpha=0.5)

# Subplot 2: G o H
axes[1].fill(
    np.real(z_boundary), np.imag(z_boundary), color="blue", alpha=0.2, label="Origineel"
)
axes[1].plot(np.real(z_boundary), np.imag(z_boundary), color="blue", lw=1.2)
trans_GH = G(H(z_boundary))
axes[1].fill(
    np.real(trans_GH),
    np.imag(trans_GH),
    color="purple",
    alpha=0.3,
    label=r"$G \circ H$",
)
axes[1].plot(np.real(trans_GH), np.imag(trans_GH), color="purple", lw=1.2)
axes[1].axhline(0, color="black", lw=0.5)
axes[1].axvline(0, color="black", lw=0.5)
axes[1].set_xlim(-5, 5)
axes[1].set_ylim(-5, 5)
axes[1].set_aspect("equal", adjustable="box")
axes[1].set_title(r"$G \circ H: z \mapsto e^{i\pi/4}(z/2)$")
axes[1].set_xlabel("Re(z)")
axes[1].set_ylabel("Im(z)")
axes[1].legend(loc="upper right", fontsize="small")
axes[1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(output_dir / "H2-1.1-oef6.pdf", bbox_inches="tight")
plt.close()
print("Saved H2-1.1-oef6.pdf")

# =============================================================
# 4. H3-3.4-oef7
# =============================================================
x = np.linspace(-4, 4, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y + 1e-10
U = np.log(np.abs(Z))
V = np.angle(Z)
V_masked = np.ma.masked_where((X < 0) & (np.abs(Y) < 0.05), V)

# 2D contour plot
plt.figure(figsize=(10, 4.5))
plt.subplot(1, 2, 1)
plt.contour(X, Y, U, levels=20, colors="blue")
plt.title(r"Level curves: $u(x,y) = \ln|z|$")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect("equal")

plt.subplot(1, 2, 2)
plt.contour(X, Y, V_masked, levels=20, colors="red")
plt.title(r"Level curves: $v(x,y) = \operatorname{Arg}(z)$")
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.gca().set_aspect("equal")

plt.tight_layout()
plt.savefig(output_dir / "H3-3.4-oef7_2d.pdf", bbox_inches="tight")
plt.close()
print("Saved H3-3.4-oef7_2d.pdf")

# 3D surface plot
U_masked = np.where(np.abs(Z) < 0.15, np.nan, U)
V_masked_3d = np.where((X < 0) & (np.abs(Y) < 0.05), np.nan, V)

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1, projection="3d")
surf1 = ax1.plot_surface(X, Y, U_masked, cmap="viridis", edgecolor="none", alpha=0.9)
ax1.set_title(r"3D Surface: Real Part $u(x,y) = \ln|z|$")
ax1.set_xlabel("Re(z)")
ax1.set_ylabel("Im(z)")
ax1.set_zlabel("u(x,y)")
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

ax2 = fig.add_subplot(1, 2, 2, projection="3d")
surf2 = ax2.plot_surface(X, Y, V_masked_3d, cmap="plasma", edgecolor="none", alpha=0.9)
ax2.set_title(r"3D Surface: Imaginary Part $v(x,y) = \operatorname{Arg}(z)$")
ax2.set_xlabel("Re(z)")
ax2.set_ylabel("Im(z)")
ax2.set_zlabel("v(x,y)")
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)
ax2.view_init(elev=30, azim=120)

plt.tight_layout()
plt.savefig(output_dir / "H3-3.4-oef7_3d.pdf", bbox_inches="tight")
plt.close()
print("Saved H3-3.4-oef7_3d.pdf")

print("All figures successfully exported!")
