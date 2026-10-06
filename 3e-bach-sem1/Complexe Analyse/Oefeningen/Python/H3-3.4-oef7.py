import numpy as np
import matplotlib.pyplot as plt

# Definieer de dimensies van het complex plane via een 2D meshgrid
# We gebruiken een hoge resolutie (500x500) voor vloeiende level curves
x = np.linspace(-4, 4, 500)
y = np.linspace(-4, 4, 500)
X, Y = np.meshgrid(x, y)

# Construeer de complexe matrix Z. 
# We voegen een extreem kleine epsilon toe aan Z om de wiskundige 
# singulariteit exact in de oorsprong (0+0j) te vermijden.
epsilon = 1e-10
Z = X + 1j * Y + epsilon

# Genereer de real part u(x,y) = ln|z|
# np.abs berekent vectorized de modulus van de gehele complexe matrix
U = np.log(np.abs(Z))

# Genereer de imaginary part v(x,y) = Arg(z)
# np.angle forceert de waarden in de array strikt binnen (-pi, pi]
V = np.angle(Z)

# Maskeer de branch cut discontinuïteit op de negatieve reële as
# Dit voorkomt dat de contour plotter interpolatielijnen tekent over de -pi naar pi sprong
V_masked = np.ma.masked_where((X < 0) & (np.abs(Y) < 0.05), V)

# Initialiseer de matplotlib figure met twee subplots naast elkaar
plt.figure(figsize=(12, 6))

# Subplot 1: Real part
plt.subplot(1, 2, 1)
# Genereer 20 contour levels. De kleur blauw wordt gebruikt voor contrast.
plt.contour(X, Y, U, levels=20, colors='blue')
plt.title(r'Level curves: Real Part $u(x,y) = \ln|z|$')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.grid(True, linestyle='--', alpha=0.6)
# Forceer een 1:1 aspect ratio zodat de cirkels niet elliptisch vervormen
plt.gca().set_aspect('equal')

# Subplot 2: Imaginary part
plt.subplot(1, 2, 2)
# Gebruik de masked array om artefacten bij de branch cut te elimineren
plt.contour(X, Y, V_masked, levels=20, colors='red')
plt.title(r'Level curves: Imaginary Part $v(x,y) = \operatorname{Arg}(z)$')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.gca().set_aspect('equal')

# Render de plot interface
plt.tight_layout()
plt.show()



# Knip de oneindige put (singularity) rond de oorsprong af. 
# Zonder deze limitatie schaalt de Z-as naar -oneindig en wordt de rest van de plot onleesbaar vlak.
U_masked = np.where(np.abs(Z) < 0.15, np.nan, U)

# Vervang de fasediscontinuïteit door NaN om de 'verticale muur' artefacten 
# in een 3D surface plot te elimineren. Matplotlib verbindt NaN-waarden niet.
V_masked = np.where((X < 0) & (np.abs(Y) < 0.05), np.nan, V)

# Initialiseer de matplotlib figure met 3D projecties
fig = plt.figure(figsize=(14, 7))

# Subplot 1: 3D Real part
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
surf1 = ax1.plot_surface(X, Y, U_masked, cmap='viridis', edgecolor='none', alpha=0.9)
ax1.set_title(r'3D Surface: Real Part $u(x,y) = \ln|z|$')
ax1.set_xlabel('Re(z)')
ax1.set_ylabel('Im(z)')
ax1.set_zlabel('u(x,y)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

# Subplot 2: 3D Imaginary part met de branch cut 'trap'
ax2 = fig.add_subplot(1, 2, 2, projection='3d')
surf2 = ax2.plot_surface(X, Y, V_masked, cmap='plasma', edgecolor='none', alpha=0.9)
ax2.set_title(r'3D Surface: Imaginary Part $v(x,y) = \operatorname{Arg}(z)$')
ax2.set_xlabel('Re(z)')
ax2.set_ylabel('Im(z)')
ax2.set_zlabel('v(x,y)')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

# Optimaliseer de weergavehoek (elevatie, azimut) voor de beste blik op de branch cut
ax2.view_init(elev=30, azim=120)

plt.tight_layout()
plt.show()