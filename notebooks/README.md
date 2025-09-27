# Notebooks

This is the directory for Jupyter notebooks.

## Run the setup

When creating a new notebook in this directory, add the following cell to execute common setup:

```python
%run setup.ipynb
```

This also works for notebooks in subdirectories. For example, say you have the following directory structure:

```bash
notebooks
├── README.md
├── setup.ipynb      # The common setup
└── experiment_1     # A directory to group similar experiments
    └── task_0.ipynb # This is your notebook
```

In `experiment_1/task_0.ipynb`, running the following cell works:

```python
%run ../setup.ipynb

import mero
```