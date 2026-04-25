# Reproducible Catalogue-Level Time-Domain Benchmarks in High-Energy Astrophysics

This repository contains the full software, data products, and manuscript-synchronization workflow used to analyse public high-energy astrophysics catalogues, including Fermi-GBM GRBs, Fermi-LAT 4LAC AGN, and AMS-02 time-dependent proton-flux data.

## Repository contents

- `data/` — input and processed data products
- `outputs/` — generated tables, figures, and LaTeX macro files
- `scripts/` — Python scripts used to run the workflow
- `notebooks/` — analysis notebooks
- `manuscript/` — manuscript-related files, if included

## Reproducibility

The workflow is designed to regenerate the main analysis outputs from public catalogue inputs. It records data provenance, writes cleaned analysis-ready tables, regenerates figures and tables, and exports numerical values to LaTeX macro files.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the workflow

```bash
python scripts/run_workflow.py
```

If your workflow uses notebooks instead of a single script, open the notebooks in order and run all cells.

## Data sources

This project uses public catalogue data from:

- Fermi-GBM GRB catalogue
- Fermi-LAT 4LAC AGN catalogue
- AMS-02 time-dependent proton-flux tables

## Citation

If you use this repository, please cite the associated manuscript and archived release.
