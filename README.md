# CSR SALAD v10.1

**Cofactor Specificity Reversal - Semi-Automated Library Design**

[![GitHub](https://img.shields.io/badge/GitHub-fhalab%2FCSR--SALAD-blue)](https://github.com/fhalab/CSR-SALAD)

A computational tool for designing site-directed mutagenesis libraries to reverse cofactor specificity in NAD(P)-dependent enzymes.

## Repository

https://github.com/fhalab/CSR-SALAD

## Overview

CSR SALAD analyzes protein-cofactor binding sites from PDB structures and designs targeted mutagenesis libraries to switch cofactor specificity between NAD and NADP. The tool:

- Identifies residues involved in cofactor binding
- Classifies residues by their interaction geometry (edge, face, bidentate, etc.)
- Generates optimized degenerate codon libraries for specificity reversal
- Suggests additional positions for activity recovery through saturation mutagenesis

## Features

- **Automated Binding Site Analysis**: Identifies first and second shell residues around NAD(P) cofactors
- **Geometric Classification**: Categorizes residues based on their 3D orientation relative to the adenine ring
- **Smart Library Design**: Generates minimal libraries within user-defined size constraints
- **Recovery Suggestions**: Identifies backing residues and hydrogen-bonding partners for activity recovery
- **Flexible Options**: Exclude/include glycine-rich motifs, diphosphate-binding residues, and peripheral residues

## Installation

### Option 1: Using Conda (Recommended)

1. Clone this repository:

```bash
git clone https://github.com/fhalab/CSR-SALAD.git
cd CSR-SALAD
```

2. Create the conda environment from the provided file:

```bash
conda env create -f environment.yml
```

3. Activate the environment:

```bash
conda activate csr-salad
```

4. Launch JupyterLab:

```bash
jupyter lab
```

### Option 2: Using pip

1. Clone this repository:

```bash
git clone https://github.com/fhalab/CSR-SALAD.git
cd CSR-SALAD
```

2. Ensure you have Python 3.8+ installed
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Launch JupyterLab:

```bash
jupyter lab
```

### Option 3: Development Installation

For development or if you want to install as a package:

1. Clone the repository:

```bash
git clone https://github.com/fhalab/CSR-SALAD.git
cd CSR-SALAD
```

2. Install in editable mode:

```bash
pip install -e .
```

## Requirements

- Python 3.8 or higher
- Biopython >= 1.79
- NumPy >= 1.20.0
- Pandas >= 1.3.0
- JupyterLab >= 3.0.0
- IPython >= 7.0.0

## Usage

### Quick Start

1. Open `CSR_SALAD_v10.1.ipynb` in JupyterLab
2. In the first cell, configure your parameters:
   - `infile`: Path to your PDB file containing the protein-cofactor complex
   - `max_size`: Maximum library size (typically 0.5× your screening capacity)
   - `ex_motif`: Exclude glycine-rich motif residues from the library
   - `ex_diphos`: Exclude diphosphate-contacting residues
   - `ex_periph`: Exclude peripheral residues
   - `verbose`: Show detailed analysis log

3. Run all cells (Cell → Run All)
4. Results will appear at the bottom showing:
   - Library design with degenerate codons
   - Site-saturation mutagenesis targets for activity recovery

### Example Configuration

```python
infile = './my_enzyme.pdb'
max_size = 400  # Target library size
ex_motif = True  # Exclude glycine-rich motif
ex_diphos = True  # Exclude diphosphate contacts
ex_periph = False  # Include peripheral residues
verbose = False  # Minimal output
```

### Input Requirements

Your PDB file must contain:
- A complete protein structure (or relevant domain)
- At least one bound cofactor molecule with residue name:
  - `NAP` or `NDP` for NADP (designing NAD→NADP library)
  - `NAD` or `NAI` for NAD (designing NADP→NAD library)

### Output

The tool generates two main outputs:

1. **Library Design Table**
   - Position and residue type
   - Binding classification (Edge, Face, Bidentate, etc.)
   - Degenerate codon for mutagenesis
   - Encoded amino acid diversity

2. **Recovery Targets Table**
   - Residues prioritized for site-saturation mutagenesis
   - Priority level (High, Medium, Low)
   - Reason for inclusion (backing residue, H-bonding, excluded from library)

## Methodology

CSR SALAD uses a geometric analysis approach:

1. **Cofactor Detection**: Identifies NAD(P) molecules in the structure
2. **First Shell Identification**: Finds residues within 4.2 Å of the 2'-phosphate moiety
3. **Geometric Classification**:
   - Transforms residue coordinates into adenine ring-centered coordinate system
   - Classifies based on 3D position (edge, face, bidentate contacts)
   - Identifies glycine-rich motifs
4. **Library Generation**:
   - Assigns pre-validated degenerate codons based on wild-type residue and geometry
   - Optimizes library size by selective inclusion/exclusion
5. **Recovery Analysis**:
   - Identifies backing residues behind the adenine ring
   - Finds second-shell charged residues
   - Detects hydrogen-bonding partners

## Citation

If you use CSR SALAD in your research, please cite:

```
CSR SALAD Version 10.1 (2025)
Adapted by Jackson Cahn
California Institute of Technology
```

Original methodology:
```
CSR SALAD Version 8 (2015)
Jackson Cahn
California Institute of Technology
```

## Troubleshooting

### Common Issues

**"Cofactor not found"**
- Ensure your PDB file contains NAP/NDP (for NADP) or NAD/NAI (for NAD)
- Check that the cofactor residue names are correctly formatted

**"No phosphate atoms found"**
- Verify that your cofactor molecule is complete in the PDB file
- Missing atoms may prevent proper analysis

**"No residues classified"**
- Try expanding the search radius by setting `ex_periph = False`
- Check that protein residues are near the cofactor binding site

**Library too large**
- Increase `max_size` parameter
- Enable exclusion options (`ex_motif`, `ex_diphos`, `ex_periph`)

## License

Copyright California Institute of Technology
All rights reserved

## Author

Jackson Cahn
California Institute of Technology

## Version History

- **v10.1** (October 2025): Updated analysis algorithms and library designs
- **v8** (December 2015): Original implementation

## Support

For questions, issues, or suggestions, please open an issue on the [GitHub repository](https://github.com/fhalab/CSR-SALAD/issues).
