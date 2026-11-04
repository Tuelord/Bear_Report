# Bear Buddy LaTeX Report Project

This project contains the complete, compilation-ready LaTeX source for the **Bear Buddy Application** Software Requirement Specification and System Architecture report, structured in accordance with the official **Ho Chi Minh City University of Technology (HCMUT - CSE)** template (`template.pdf`).

---

## 1. Project Directory Structure

```text
D:\WorkSpace\report\
├── main.tex                    # Primary document driver (geometry, fonts, headers, TOC)
├── cover.tex                   # Official HCMUT cover page (double border, university logo)
├── contributions.tex           # Member Contributions table (page ii)
├── references.bib              # Complete BibTeX bibliography (18 academic & clinical sources)
├── figures/                    # High-resolution 300 DPI diagram images
│   ├── hcmut_logo.png          # HCMUT University Logo
│   ├── use_case_diagram.png    # Figure 3.1: Use Case Diagram
│   ├── context_diagram.png     # Figure 3.2: System Context Diagram
│   ├── dfd_level_0.png         # Figure 3.3: Level 0 Data Flow Diagram
│   ├── story_five_stages.png   # Figure 4.1: Five Structural Stages of a Social Story
│   ├── system_architecture.png # Figure 6.1: Three-Layer Offline-First Architecture
│   ├── sqlite_erd.png          # Figure 6.2: SQLite Entity-Relationship Diagram
│   ├── sequence_story_learning.png # Figure 6.3: Story Learning Sequence Diagram
│   ├── sequence_voice_interaction.png # Figure 6.4: Scenario E Voice Interaction Sequence Diagram
│   └── state_machine.png       # Figure 6.5: Story Player State Machine Diagram
└── chapters/
    ├── chapter1.tex            # Chapter 1: Introduction
    ├── chapter2.tex            # Chapter 2: Background and Related Work
    ├── chapter3.tex            # Chapter 3: Requirement Analysis
    ├── chapter4.tex            # Chapter 4: Story Content and Interaction Design
    ├── chapter5.tex            # Chapter 5: UI/UX Design
    └── chapter6.tex            # Chapter 6: System Architecture and Design
```

---

## 2. Formatting & Typography Specifications

- **Language**: 100% Academic English across all chapters, tables, and frontmatter.
- **Diagrams**: All 9 architectural and behavioral diagrams are provided as dedicated **300 DPI PNG images** in `figures/`, included via `\includegraphics[width=...]{figures/...}` for fast, standalone, and reliable compilation.
- **Margins & Page Setup**: A4 Paper, Left $30\text{ mm}$, Right $20\text{ mm}$, Top $20\text{ mm}$, Bottom $20\text{ mm}$ (Standard HCMUT thesis/report regulations).
- **Typography**: Times New Roman, $12\text{ pt}$ body text, $1.5$ line spacing (`\onehalfspacing`).
- **Page Numbering**:
  - Frontmatter (Cover, Contributions, TOC, List of Figures, List of Tables): Lowercase Roman numerals (`i`, `ii`, `iii`, ...).
  - Main Body (Chapters 1--6): Arabic numerals (`1`, `2`, `3`, ...) centered in the footer.
- **Tables**: Built using `xltabular`, supporting automatic multi-page breaks, repeated headers (`\endhead`), and strict grid borders.

---

## 3. How to Compile to PDF

### Option A: Overleaf (Recommended)
1. Compress all files in `d:\WorkSpace\report\` (the `.tex` files, `.bib`, `chapters/` folder, and `figures/` folder) into a single `.zip` archive.
2. Log in to [Overleaf](https://www.overleaf.com), click **New Project** $\rightarrow$ **Upload Project**, and upload the `.zip` archive.
3. In the Overleaf **Menu** (top-left corner):
   - Set **Compiler**: `XeLaTeX` (or `pdfLaTeX`).
   - Set **Main document**: `main.tex`.
4. Click **Recompile** to produce the final PDF.

### Option B: Local Compilation (Command Line / VS Code)
Open PowerShell or Terminal in `D:\WorkSpace\report\` and execute:
```bash
xelatex main.tex
bibtex main
xelatex main.tex
xelatex main.tex
```
*(Or replace `xelatex` with `pdflatex`).*
