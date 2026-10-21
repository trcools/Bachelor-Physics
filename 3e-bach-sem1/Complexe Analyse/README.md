# Complexe Analyse (Complex Analysis)

Comprehensive study resources, exercise solutions, LaTeX lecture notes, and Python visualization scripts for **Complexe Analyse** (3rd Bachelor Physics & Astronomy).

---

## 📂 Directory Structure

```text
Complexe Analyse/
├── Cursus/             # Official syllabus / lecture notes
├── Examens/            # Past exam problems and formulations
├── Moeilijkheden/      # Deep dive into conceptual bottlenecks and challenging exercises
│   ├── Moeilijkheden-oef-complexe.tex   # LaTeX compilation of tricky problem walkthroughs
│   ├── Moeilijkheden-theorie.tex        # Theoretical proofs and challenging derivations
│   └── figuren-voor-oef/                # Generated visual figures for exercise analysis
├── Oefeningen/         # Problem sets and numerical/analytical solutions
│   └── Python/         # Python plotting & conformal mapping visualization scripts
└── Theorie/            # Complete LaTeX textbook rewrite and theory visualizations
    ├── Code/           # Visual scripts for complex trigonometric & periodic functions
    └── Cursus/         # Modular LaTeX book structure (Chapters 1 to 7)
        ├── chapters/   # Modular chapters (ch1 to ch7)
        └── main.tex    # Master LaTeX document
```

---

## 📘 Course Content & Chapters

The theoretical notes cover:
1. **Chapter 1: Complex Numbers** (`ch1_complex_numbers.tex`) — Algebraic properties, polar representation, roots of unity, topology of the complex plane.
2. **Chapter 2: Analytic Functions** (`ch2_analytic_functions.tex`) — Limits, continuity, complex differentiability, Cauchy-Riemann equations, harmonic functions.
3. **Chapter 3: Elementary Functions** (`ch3_elementary_functions.tex`) — Exponential, trigonometric, hyperbolic functions, complex logarithm, branch cuts and Riemann surfaces.
4. **Chapter 4: Complex Integration** (`ch4_complex_integration.tex`) — Contour integrals, Cauchy-Goursat theorem, Cauchy's integral formulas, Liouville's theorem, Fundamental Theorem of Algebra.
5. **Chapter 5: Series Representations** (`ch5_series_representations.tex`) — Taylor series, Laurent series, classification of singularities (poles, essential singularities, removable singularities).
6. **Chapter 6: Residue Theory** (`ch6_residue_theory.tex`) — Residue theorem, calculation of residues, evaluation of real integrals and principal values, Jordan's lemma.
7. **Chapter 7: Conformal Transformations** (`ch7_transforms.tex`) — Conformal mapping properties, Möbius / bilinear transformations, physical applications.

---

## 🐍 Python Visualizations (`Oefeningen/Python/`)

Custom Python visualization tools for key exercises:
- `export_alle_figuren.py`: Batch script to regenerate all plots and save them into `Moeilijkheden/figuren-voor-oef/`.
- `H1-1.5-oef7.py`: Visualizing geometric loci and complex plane sets.
- `H2-1.1-oef4.py` & `H2-1.1-oef6.py`: Cauchy-Riemann verification and conformal mapping grids.
- `H3-3.4-oef7.py`: 2D and 3D surface visualizations of multivalued logarithmic and power branches.
- `H4-4.1-oef1.py`, `H4-4.6-oef1.py`, `H4-4.6-oef2.py`: Contour integration curves and residue contributions.

### Running the Python Visualizations

```bash
# Activate your environment
source ../../.venv/bin/activate

# Run an individual visualization
python "Oefeningen/Python/H3-3.4-oef7.py"

# Or batch export all figures
python "Oefeningen/Python/export_alle_figuren.py"
```

---

## 📝 Compiling the Theory Notes

The theory notes in `Theorie/Cursus/` can be compiled using `latexmk` or `pdflatex`:

```bash
cd "Theorie/Cursus"
latexmk -pdf main.tex
# Clean up temporary build files:
latexmk -c
```
