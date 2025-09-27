# Mean vs. Robust Aggregators on Distributed Heterogeneous Data

_No, Mean Aggregator is not more Robust than Robust Aggregators under reasonable assumptions._

## Development

The installation instructions below are compatible with Linux, MacOS and WSL.

### With [`uv`](https://docs.astral.sh/uv) (recommended)

#### Install the dependencies

Create the virtual environment:

```bash
uv lock
uv sync
```

#### Activate the virtual environment

Whenever you need to run a Python command, activate the virtual environment with:

```bash
uv venv
source .venv/bin/activate
```

#### Update the `pip` requirements

Whenever installing a new dependency, update the `requirements.txt` with the following command:

```bash
uv pip freeze > requirements.txt
```

### With `venv`

This project is also compatible with other virtual environment managers, such as `venv`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### Update the `pip` requirements

Whenever installing a new dependency, update the `requirements.txt` with the following command:

```bash
pip freeze > requirements.txt
```

### Directory structure

```bash
├── data             # Downloaded datasets
├── mero             # Shared Python module for notebooks and scripts
│   ├── aggregators  # Implemented gradient aggregators
│   ├── attacks      # Data poisoning attacks
│   ├── datasets     # Used datasets
│   ├── metrics      # Gradient metrics (heterogeneity, disturbance...)
│   ├── modeling     # Models and training hyperparameters
│   └── plots        # Code for plotting figures
├── checkpoints      # Model checkpoints
├── notebooks        # Jupyter notebooks for simple code and visualization
├── reports          # Experimental results
│   └── figures      # PDF and PNG figures
├── scripts          # Long-running, parallel scripts
```
