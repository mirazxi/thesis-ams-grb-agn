# thesis-ams-grb-agn

Code + analysis for thesis figures/tables (AMS-02 / GRB / AGN).

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt



### requirements.txt (auto-generate from your current env)
# Reproducible Catalogue-Level Time-Domain Benchmarks for Extreme Particle Acceleration

[![License](https://img.shields.io/badge/license-see%20LICENSE-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![Status](https://img.shields.io/badge/status-research%20code-orange.svg)]()
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18684545.svg)](https://doi.org/10.5281/zenodo.18684545)

This repository contains the full software, data products, and manuscript-synchronization workflow used to analyze **Fermi-GBM GRBs**, **Fermi-LAT 4LAC AGN**, and **AMS-02 time-dependent proton-flux data**.

The project is built as an end-to-end **code-to-paper reproducibility pipeline**: cleaned datasets, processed CSV tables, summary statistics, regenerated figures, and manuscript numbers are produced from the same analysis workflow, with selected numerical results exported into LaTeX macro files for direct manuscript use.

---

## Overview

This repository supports a reproducible catalogue-level benchmark study of extreme particle acceleration across three public high-energy astrophysical datasets:

- **Fermi-GBM burst catalogue** for GRB prompt-emission duration statistics
- **Fermi-LAT 4LAC catalogue** for AGN spectral and variability diagnostics
- **AMS-02 time-dependent proton-flux tables** for cosmic-ray modulation and time-domain variability analysis

The workflow is designed to:

- ingest public astrophysical catalogue products
- clean and standardize them into analysis-ready tables
- compute benchmark summary statistics
- regenerate manuscript figures and tables
- export manuscript-ready LaTeX macro values
- keep the paper synchronized with the underlying analysis

A central operational quantity in the benchmark is the AMS-02 fractional amplitude

\[
A = \frac{J_{\max} - J_{\min}}{\langle J \rangle},
\]

used as a transparent reference scale for contextualizing catalogue-defined AGN variability amplitudes on a common dimensionless axis.

---

## What this repository is used for

This repository is intended for:

### 1. Reproducing the benchmark analysis
Users can reproduce the cleaned datasets, summary tables, and figure-generation workflow starting from public input data.

### 2. Regenerating manuscript results
The repository supports regeneration of:

- processed CSV tables
- summary output tables
- manuscript figures
- LaTeX macro files containing reported numerical values

### 3. Auditing and verifying reported values
The code and exported data products allow readers, collaborators, and referees to trace reported values back to the processed datasets and analysis logic.

### 4. Extending the project
The workflow can be adapted for:

- updated public catalogue releases
- new rigidity-bin studies
- alternative variability estimators
- additional robustness checks
- related catalogue-level astrophysical benchmark studies

In short, this repository is not only a code archive. It is the **full computational workflow behind the paper**.

---

## Main contributions of the repository

- standardized ingestion of multiple public high-energy datasets
- transparent separation of raw, interim, processed, and output data layers
- reproducible generation of analysis-ready CSV tables
- regeneration of summary tables and manuscript figures
- export of manuscript numerical values into LaTeX macros
- reusable code-to-paper framework for future benchmark studies

---

## Software used

This project was developed in a **Python-based scientific computing environment**.

### Core software stack

- **Operating system:** Ubuntu / Linux environment
- **Programming language:** Python 3
- **Interactive analysis environment:** Jupyter Notebook

### Main Python packages

The workflow uses scientific Python tools including:

- `numpy`
- `pandas`
- `scipy`
- `matplotlib`
- `astropy`
- `jupyter`

The exact installable package list for this repository is provided in:

```text
requirements.txt
