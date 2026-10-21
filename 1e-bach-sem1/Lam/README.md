# Lineaire Algebra en Meetkunde (LAM)

Study materials, theorem overviews, proofs, counterexamples, and interactive Jupyter notebooks for **Lineaire Algebra en Meetkunde** (1st Bachelor Physics & Astronomy, Course Code `C004606A`).

---

## 📂 Directory Structure

```text
Lam/
├── Bewijzen/                               # Comprehensive LaTeX document with course proofs
│   ├── main.tex                            # Master document combining all proofs
│   └── H1_LAM.tex ... H8_LAM.tex           # Proofs separated per chapter
├── C004606A - Lineaire algebra - .../      # Course reference materials & outlines
├── examens-lam/                            # Exam questions, photo captures, and exam attempts
│   └── LAM-examens-pogingen.tex
├── H3-Lineaire-Afbeeldingen/               # Linear maps, kernel, image, dimension theorem
│   └── dimensie-homomorfisme.ipynb         # Interactive rank-nullity & homomorphism notebook
├── H4-Coordinaten/                         # Coordinates & base change
│   └── voorstelling-coordinatentransofrmatie.ipynb
├── H5-Matricees-en-Determinanten/          # Matrices, determinants & affine subspaces
│   └── Affiene-deeelruimten.ipynb
├── H8-iproduct-ruimten/                    # Inner product spaces, orthogonality, distances
│   ├── afstanden.ipynb
│   └── karakteristiek.ipynb
├── LAM-stellingen-overzicht.tex            # Full overview of all theorems to know
├── LAM_definities.tex                      # Core definitions summary
└── LAM_tegenvoorbeelden.tex                # Instructive counterexamples (crucial for multiple-choice/oral exams)
```

---

## 📘 Chapters Overview

1. **Vectoren en Vectorruimten** — Vector space axioms, linear combinations, linear independence, spanning sets, bases, and dimension.
2. **Deelruimten en Sommen** — Subspaces, direct sums, Grassmann's dimension formula.
3. **Lineaire Afbeeldingen** — Homomorphisms, kernel and image, rank-nullity theorem (dimensiestelling), isomorphisms.
4. **Coördinaten en Basistransformaties** — Coordinate vectors, transformation matrices, change of basis commutative diagrams.
5. **Matrices en Determinanten** — Matrix calculus, row reduction, determinant definitions, cofactor expansion, Cramer's rule, affine subspaces.
6. **Stelsels Lineaire Vergelijkingen** — Rouché-Capelli theorem, Gaussian elimination.
7. **Eigenwaarden en Eigenvectoren** — Characteristic polynomial, eigenspaces, geometric and algebraic multiplicity, diagonalizability.
8. **Inwendig-Productruimten (Euclidische & Hermitische ruimten)** — Inner products, Cauchy-Schwarz inequality, Gram-Schmidt orthogonalization, orthogonal projections, adjoint operators.
9. **Symmetrische en Unitaire Operatoren** — Spectral theorem for self-adjoint operators, quadratic forms, singular value decomposition (SVD).

---

## 🐍 Interactive Notebooks

Launch Jupyter to explore the interactive visual demonstrations:
```bash
jupyter lab "H3-Lineaire-Afbeeldingen/dimensie-homomorfisme.ipynb"
```
