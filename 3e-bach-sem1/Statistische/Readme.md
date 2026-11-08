# Statistische Fysica (Statistical Physics)

## Examenstof
i) Hoofdstuk 1 tot en met Hoofdstuk 6: volledig + artikel "Negative Absolute Temperatures"
ii) Hoofdstuk 7: paragraaf 7.1, paragraaf 7.2.1 en paragraaf 7.2.3
iii) Hoofdstuk 8 tot en met Hoofdstuk 10: volledig buiten paragraaf 10.5
iv) Hoofdstukken 11 en 12: volledig
v) Hoofdstuk 13: paragrafen 13.1, 13.2, 13.3
vi) Appendix A en Appendix B


## Verzameling van de afleidingen:
 - H2:
    - 2.3:
      - Afleiding, equivalente definitie entropie Eq. (2.11)
      - Eigenschappenn van Entropie
    - 2.4:
      - Schottky defecten in functie van temperatuur
    - 2.5:
      - Veralgemeend equipartitie theorema Eq. (2.41)
      - Viriaal theorema Eq. (2.49)
    - 2.6:
      - Theorema van Liouville Eq. (2.60) - Eq. (2.60)
      - Gevolgen van Liouville theorema
    - 2.7:
      - Systeem in warmtebad theorie Pg. (30-33)
      - Veralgemening entropie

 - H7:
    - 7.2.1:
      - Gesloten uitdrukking voor gemiddelde waarde $\bar{h}$ Eq. (7.3)
    - 7.2.3:
      - De drukvergelijking Eq. (7.18)
  - H8:
    - 8.3:
      - Partitiefunctie van een ideaal kwantumgas Eq. (8.13) ? (klein)
    - 8.4:
      - Bewijs positief definitiet van dichtheidsmatrix Eq. (8.25)
      - Equivalent Liouville (tijdsevolutie vd faseruimtedichtheid) Eq. (8.26-8.27)
  - H9:
    - 9.2:
      - Afleiding partititiefunctie fotonengas
   - 9.3:
      - Afleiding Stralingswet van Planck
      - Wet van Stefan-Boltzmann
      - Vrije energie en druk van fotonengas

> ### 📝 Tips Oefeningenexamen (Notities uit de werkcolleges)
>
> Op het examen wordt vaak gepeild naar volgende situaties:
> - **Lage $T$**: $F \approx E \to S \approx 0$
> - **Hoge $T$**: $S \gg$
>
> **Wat we vanbuiten moeten kennen:**
> In welke systemen (met welke variabelen) we welke eenheden we moeten maximaliseren of minimaliseren:
> - **$(T,V,N)$-systeem**: $F = E - TS$ minimaliseren!
> Thermische golflengte: $\lambda = \frac{h}{\sqrt{2\pi m k T}}$ **Vanbuiten kennen!**

Lecture notes, computational simulations, problem sets, literature articles, and exam preparation for **Statistische Fysica** (3rd Bachelor Physics & Astronomy).

---

## 📂 Directory Structure

```text
Statistische/
├── Artikels/       # Influential literature papers (BEC, Gibbs Paradox, Pauli Blocking, etc.)
├── Code/           # Computational models and Jupyter notebooks (Bose-Einstein, Fermi gas, Debye, etc.)
│   ├── B2Coefficient.ipynb   # Second virial coefficient computation
│   ├── BoseGas.ipynb         # Bose-Einstein condensation & thermodynamics
│   ├── debye.ipynb           # Debye model for specific heat of solids
│   ├── FermiGas.ipynb        # Degenerate Fermi gas & Fermi-Dirac distributions
│   ├── Paramagnetism.ipynb   # Brillouin function and Curie-Weiss law
│   └── nifd.gnuplot          # Gnuplot visualization scripts
├── Cursus/         # Course syllabi & reference textbooks (Mandl, Kardar)
├── Examens/        # Previous examination collections (since 2011) & formula sheets
├── Oefeningen/     # Problem sets divided into Reeks 1 through 7 with notebooks & solution scripts
├── Slides/         # Official course lecture slides
└── Theorie/        # Comprehensive theoretical LaTeX notes
    └── MyTheory.tex          # LaTeX compilation of statistical mechanics theory
```

---

## 💡 Exam Tips & Key Theoretical Relations

> [!IMPORTANT]
> **Key thermodynamic potentials to minimize / maximize per ensemble:**
> - **Canonical $(T, V, N)$ system**: Helmholtz free energy $F = E - TS$ is **minimized** at equilibrium.
> - **Microcanonical $(E, V, N)$ system**: Entropy $S$ is **maximized** at equilibrium.
> - **Grand Canonical $(T, V, \mu)$ system**: Grand potential $\Phi = F - \mu N = -pV$ is **minimized**.
> - **Isothermal-Isobaric $(T, p, N)$ system**: Gibbs free energy $G = E - TS + pV$ is **minimized**.

### Asymptotic Limits
- **Low temperature limit ($T \to 0$):**
  $$F \approx E \implies S \to 0 \quad (\text{Third Law of Thermodynamics})$$
- **High temperature limit ($T \to \infty$):**
  $$F \approx -TS \quad (\text{Entropy dominates})$$

---

## 🐍 Computational Physics Notebooks (`Code/`)

To explore the numerical models and reproduce the thermodynamic plots:

```bash
# Activate workspace virtual environment
source ../../.venv/bin/activate

# Launch Jupyter Lab
jupyter lab Code/
```

Key models explored:
- **`BoseGas.ipynb`**: Numerical evaluation of Bose-Einstein integrals $g_{3/2}(z)$ and $g_{5/2}(z)$, condensation temperature $T_c$, and heat capacity discontinuity.
- **`FermiGas.ipynb`**: Chemical potential shift $\mu(T)$, Sommerfeld expansion, and comparison with classical Maxwell-Boltzmann limit.
- **`debye.ipynb`**: High-temperature Dulong-Petit limit vs. low-temperature $T^3$ behavior.
- **`B2Coefficient.ipynb`**: Calculation of the second virial coefficient $B_2(T)$ for hard-sphere and Lennard-Jones potentials.

---

## 📝 Compiling the Theory Notes

```bash
cd Theorie
pdflatex MyTheory.tex
```
