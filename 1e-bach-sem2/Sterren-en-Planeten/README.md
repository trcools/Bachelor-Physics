# Sterren en Planeten (Stars and Planets)

Study notes, essential derivations, formula sheets, and practical calculation tips for **Sterren en Planeten** (1st Bachelor Physics & Astronomy, Course Code `C004206A`).

---

## 📂 Directory Structure

```text
Sterren-en-Planeten/
├── Afleidingen_Te_Kennen.md   # Core theoretical derivations required for the exam
├── handige-tips-oef.tex       # Comprehensive LaTeX cheatsheet: spherical astronomy & exercise tips
├── weetjes_H2.tex             # Chapter 2 notes: Spherical astronomy & coordinate systems
├── weetjes_H5.tex             # Chapter 5 notes: Radiation, magnitudes & stellar parameters
└── Sterren_en_Planeten.txt    # Summary notes and problem walkthroughs
```

---

## 📘 Topics Covered

1. **Sferische Sterrenkunde (Spherical Astronomy)**:
   - Coordinate systems: Horizontal $(A, a)$, Equatorial $(h, \delta)$ / $(\alpha, \delta)$, Ecliptic $(\lambda, \beta)$.
   - Spherical trigonometry (sine rule, cosine rule for spherical triangles).
   - Sidereal time ($\Theta = h + \alpha$), solar time, equation of time.
   - Culmination ($h=0^\mathrm{h}$ upper, $h=12^\mathrm{h}$ lower), circumpolar conditions, sunrise and sunset hour angles.
   - Observational corrections: atmospheric refraction, annual and diurnal aberration, trigonometric parallax.

2. **Straling & Stellaire Parameters (Radiation & Stellar Properties)**:
   - Blackbody radiation, Planck's law, Wien's displacement law, Stefan-Boltzmann law.
   - Apparent and absolute magnitudes, distance modulus ($m - M = 5\log_{10}(d) - 5$).
   - Bolometric magnitude and luminosity ($L = 4\pi R^2 \sigma T_\text{eff}^4$).
   - Color indices ($B-V$) and interstellar extinction ($A_V$).
   - Spectral classification (OBAFGKM) and the Hertzsprung-Russell (HR) diagram.

---

## 📝 Compiling the Cheatsheet

```bash
pdflatex handige-tips-oef.tex
```

