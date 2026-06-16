# Ἡ Κοινὴ καθ᾿ αὑτὴν φωτιζομένη (KPSI)

An LLPSI-style inductive graded reader for New Testament Koine Greek. Original continuous Greek narrative set in Corinth, 50s AD — no translation, no vocabulary lists — designed to carry the reader inductively from zero to the real NT text.

---

## Prerequisites (macOS)

### 1. Homebrew

All other tools are easiest to install via [Homebrew](https://brew.sh).

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### 2. Pandoc

Required by **all three build scripts** (`html.sh`, `pdf.sh`, `ebook.sh`).

```bash
brew install pandoc
```

Verify: `pandoc --version`

---

### 3. MacTeX (for PDF output only)

Required by `pdf.sh`. Provides the `xelatex` engine and the LaTeX packages used in the template (`fontspec`, `polyglossia`, `csquotes`, `microtype`, `hyperref`).

```bash
brew install --cask mactex
```

> MacTeX is a large download (~4 GB). After installation, open a new terminal session so that `xelatex` is on your `PATH`.

Verify: `xelatex --version`

**Alternative:** If you already have TeX Live, ensure it includes `xelatex` and the packages above (all are part of a full TeX Live install).

---

### 4. SBL Greek font (for PDF output only)

The LaTeX template sets `SBL Greek` as the main font for rendering polytonic Greek. MacTeX bundles it, but verify it is visible to the system font cache:

```bash
fc-list | grep -i "sbl"
```

If it is missing, rebuild the font cache after installing MacTeX:

```bash
sudo fc-cache -fv
```

If it is still missing, download and install it manually from [SIL International](https://software.sil.org/sblgreek/).

---

### 5. Python 3 (for vocabulary checker only)

Required by `scripts/vocab_check.py`. Python 3 ships with macOS 12.3 and later.

```bash
python3 --version
```

If not present:

```bash
brew install python
```

No additional pip packages are needed — the script uses only the Python standard library.

---

## Building

### HTML

Converts all chapters in `src/` to HTML in `docs/`:

```bash
bash scripts/html.sh
```

### PDF

Produces `docs/kpsi.pdf` via XeLaTeX (runs twice to build the table of contents):

```bash
bash scripts/pdf.sh
```

### EPUB

Produces `docs/kpsi.epub`:

```bash
bash scripts/ebook.sh
```

### Vocabulary checker

Reports new lemmas per chapter, NT-500 coverage, and words at risk of atrophy:

```bash
python3 scripts/vocab_check.py
python3 scripts/vocab_check.py --chapter 1
python3 scripts/vocab_check.py --atrophy-threshold 4
```

> **Note:** The lemmatiser currently uses a stub (lowercasing only). For accurate NT-500 coverage numbers, wire in a real morphological analyser such as [CLTK](https://cltk.org) or [greek-lemmatization](https://pypi.org/project/greek-lemmatization/).

---

## Project structure

```
src/              ← chapter source files (Markdown)
docs/             ← built output (HTML, PDF, EPUB)
scripts/          ← build scripts and vocabulary checker
templates/        ← Pandoc HTML and LaTeX templates
```
