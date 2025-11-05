# lossers

Research code and notebooks for the lossers 'UofT Foundation Models for Science - Hackathon Project'

conformal prediction and sequence classification experiments (DNA / BERT pipelines).

This repository contains notebooks, scripts and data used to explore uncertainty quantification and conformal prediction on sequence data. It appears to include outputs from experiments (predictions and probabilities), several notebooks for training and analysis, and helper scripts.

## Repository structure

- `conformal.py` — script for conformal procedures and evaluation (inspection recommended before running).
- `conformal.ipynb`, `HV.ipynb`, `MT_dna-bert-import.ipynb`, `sdtemple_dna_bert.ipynb`, etc. — analysis and tutorial notebooks.
- `data/` — source sequence files and cleaned datasets:
  - `sequence-cleaner.tsv`
  - `sequence-filtered.tsv`
  - `sequence-wide.tsv`
  - `sequence.txt`
- `y_val_*.npy`, `y_test_*.npy`, `conformity_sets.npy` — saved numpy arrays with predictions, labels and conformity sets used for evaluation.
- `tutorials/` — additional notebooks for data extraction, fine-tuning, latent space analysis and UQ examples.

## Quick start

These are high-level instructions — inspect the notebooks and `conformal.py` to confirm exact usage and arguments before running.

1. Create a Python environment (recommended Python 3.8+).

   # Example (create env & activate)
   python -m venv .venv
   source .venv/bin/activate

2. Install the project dependencies. There is no `requirements.txt` in the repo by default; add one if you want reproducible installs. Typical packages used in these notebooks include: `numpy`, `pandas`, `scikit-learn`, `torch`/`transformers` (if using BERT models), `scipy`, `matplotlib`, `jupyter`.

   # Example (install common packages)
   pip install numpy pandas scikit-learn matplotlib jupyter

3. Open the notebooks with Jupyter or JupyterLab to explore:

   jupyter lab

   - Start with `tutorials/Data_Extraction.ipynb` to understand data layout.
   - Use `setup_train_test_split.ipynb` to prepare train/validation/test splits.
   - `conformal.ipynb` and `conformal.py` show conformal evaluation workflows.

4. If you prefer running the `conformal.py` script directly, inspect the top of the file to view CLI/parameters and call it with appropriate paths to prediction arrays and labels.

## Notebooks of interest

- `setup_train_test_split.ipynb` — split creation and dataset prep.
- `conformal.ipynb` — conformal prediction examples and analysis.
- `Fine_Tune_Model.ipynb` (under `tutorials/`) — fine-tuning a sequence model (likely uses transformers).

## Data

The `data/` folder contains TSV and text sequence files. Some notebooks expect the cleaned or filtered versions. Large model artifacts or external raw datasets are not included here; follow the notebook instructions for reproducing model training if required.

Input/Output arrays in the root (for example `y_test_pred_proba.npy`, `y_test_true.npy`) appear to store predicted probabilities and true labels used for downstream conformal evaluation.

## Notes, assumptions, and safety

- Assumption: Python 3.8+ and common ML/data packages are sufficient. If you plan to run BERT fine-tuning or inference, install `transformers` and `torch` compatible with your GPU/OS.
- Inspect notebooks and `conformal.py` before running — some scripts may expect specific file paths or environments.

## Suggested next steps (optional)

1. Add a `requirements.txt` or `pyproject.toml` for reproducible environment setup.
2. Add short usage examples and CLI flags to `conformal.py` (if missing) so the script can be run from the command line.
3. Add small smoke tests or a minimal runner script demonstrating how to load `y_test_pred_proba.npy` and compute the conformal metrics.
4. Add a CONTRIBUTING.md if you expect external contributions.

## License

This repository contains a `LICENSE` file at the repository root. Follow the terms described there.

## Contact

For questions about the code or experiments, open an issue in this repository or contact the repository owner (see git history / project hosting for contact details).

---

If you'd like, I can also:
- create a `requirements.txt` with the packages inferred from notebooks,
- add a tiny example script that loads `y_test_*` arrays and runs a conformal evaluation,
- or add a short CONTRIBUTING.md — tell me which and I'll implement it next.
