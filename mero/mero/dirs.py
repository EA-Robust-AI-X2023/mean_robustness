from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent.absolute() # The project root directory

CHECKPOINTS_DIR = ROOT_DIR / "checkpoints" # Model checkpoints directory
DATA_DIR = ROOT_DIR / "data"               # Datasets directory
FIGURES_DIR = ROOT_DIR / "reports/figures" # Figures directory