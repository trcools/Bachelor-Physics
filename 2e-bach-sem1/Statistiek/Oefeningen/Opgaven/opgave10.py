import numpy as np
import matplotlib.pyplot as plt

# Instellingen voor reproduceerbaarheid
np.random.seed(42)

# De theoretische functie (Probability Density Function)
def f(x):
    # C = 2/3, f(x) = C * (1 + x)
    return (2/3) * (1 + x)

# ---------------------------------------------------------
# 1. Simulatie: Inverse Transformatie Methode
# ---------------------------------------------------------
N_inv = 100000  # Aantal punten voor een mooi histogram
u = np.random.uniform(0, 1, N_inv)
# Formule: x = sqrt(1 + 3u) - 1
x_inverse = np.sqrt(1 + 3 * u) - 1

# ---------------------------------------------------------
# 2. Simulatie: Hit and Miss (Verwerpings) Methode
# ---------------------------------------------------------
N_hitmiss = 2000  # Minder punten voor de scatterplot (anders wordt het een vlek)
x_candidates = np.random.uniform(0, 1, N_hitmiss)
y_candidates = np.random.uniform(0, 4/3, N_hitmiss) # y tussen 0 en f_max (4/3)

accepted_x = []
accepted_y = []
rejected_x = []
rejected_y = []

for x, y in zip(x_candidates, y_candidates):
    if y <= f(x):
        accepted_x.append(x)
        accepted_y.append(y)
    else:
        rejected_x.append(x)
        rejected_y.append(y)

# ---------------------------------------------------------
# 3. Het tekenen van de figuren
# ---------------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# --- Figuur Links: Inverse Transformatie (Histogram) ---
# Plot het histogram van de gegenereerde data
count, bins, ignored = ax[0].hist(x_inverse, bins=50, density=True, 
                                  alpha=0.6, color='skyblue', label='Gesimuleerde data (Inverse)')

# Plot de theoretische curve eroverheen
x_plot = np.linspace(0, 1, 100)
ax[0].plot(x_plot, f(x_plot), linewidth=3, color='navy', label='Theoretische p.d.f. $f(x)$')

ax[0].set_title('Inverse Transformatie Methode\n(Verdeling van gegenereerde getallen)', fontsize=14)
ax[0].set_xlabel('$x$', fontsize=12)
ax[0].set_ylabel('Dichtheid', fontsize=12)
ax[0].legend()
ax[0].grid(True, alpha=0.3)

# --- Figuur Rechts: Hit and Miss (Scatterplot) ---
# Plot de verworpen punten
ax[1].scatter(rejected_x, rejected_y, color='red', s=10, alpha=0.5, label='Verworpen (Miss)')
# Plot de geaccepteerde punten
ax[1].scatter(accepted_x, accepted_y, color='green', s=10, alpha=0.5, label='Geaccepteerd (Hit)')

# Plot de curve grens
ax[1].plot(x_plot, f(x_plot), linewidth=3, color='black', label='$f(x) = \\frac{2}{3}(1+x)$')
# Teken de "doos" (enveloppe)
ax[1].hlines(4/3, 0, 1, colors='orange', linestyles='--', label='Enveloppe ($y=4/3$)')

ax[1].set_title('Hit and Miss Methode\n(Acceptatie vs. Verwerping)', fontsize=14)
ax[1].set_xlabel('$x$', fontsize=12)
ax[1].set_ylabel('$y$ (hulpvariabele)', fontsize=12)
ax[1].set_ylim(0, 1.4)
ax[1].legend(loc='lower right')
ax[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
