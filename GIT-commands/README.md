# Git Commands & Cheatsheet

Helpful Git workflows, shortcuts, and commands frequently used when working with this repository, Jupyter Notebooks, and LaTeX documents.

Interactive learning resource:
- [Learn Git Branching](https://learngitbranching.js.org) — Interactive visual tutorial for mastering branching and merging.

---

## 🚀 Daily Workflow Quick Reference

### 1. Checking Status & Staging
```bash
# Check modified, staged, and untracked files
git status

# View diff of unstaged changes
git diff

# View diff of staged changes
git diff --staged

# Stage specific files (avoid git add . to prevent committing accidental artifacts)
git add path/to/file.py
```

### 2. Committing & Branching
```bash
# Commit staged files with an informative message
git commit -m "feat(complexe-analyse): add chapter 4 contour integration notes"

# Create and switch to a new feature branch
git switch -c feature/new-course-notes

# Switch between existing branches
git switch main
```

---

## 🧹 Repository Hygiene & Housekeeping

### Cleaning untracked LaTeX artifacts
```bash
# Preview what would be deleted
git clean -ndX

# Delete untracked and ignored build files (like .aux, .log, .synctex.gz)
git clean -fdX
```

### Un-tracking an accidentally committed file (without deleting it locally)
```bash
# Remove from Git cache but keep on local disk:
git rm --cached path/to/file.pdf

# Ensure it is in .gitignore:
echo "path/to/file.pdf" >> .gitignore

# Commit the removal
git commit -m "chore: stop tracking local pdf file"
```

### Handling Jupyter Notebooks
Before committing Jupyter notebooks, it is good practice to clear the cell outputs to keep Git diffs clean:
```bash
# In VS Code: click "Clear All Outputs" in the notebook toolbar
# Or via CLI:
jupyter nbconvert --clear-output --inplace notebook.ipynb
```

---

## 📓 Interactive Notebook Cheatsheet

See [`Git_commands_cheatsheet.ipynb`](Git_commands_cheatsheet.ipynb) for interactive demonstrations and examples.
