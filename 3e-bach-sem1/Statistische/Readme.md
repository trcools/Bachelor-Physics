# Statistische Fysica (Statistical Physics)

> ### 📝 Tips Oefeningenexamen (Notities uit de werkcolleges)
>
> Op het examen wordt vaak gepeild naar volgende situaties:
> - **Lage $T$**: $F \approx E \to S \approx 0$
> - **Hoge $T$**: $S \gg$
>
> **Wat we vanbuiten moeten kennen:**
> In welke systemen (met welke variabelen) we welke eenheden we moeten maximaliseren of minimaliseren:
> - **$(T,V,N)$-systeem**: $F = E - TS$ minimaliseren!

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