import importlib.util
from pathlib import Path

# Load theory-of-everything-simulations/theory_of_everything_app.py
base_dir = Path(__file__).resolve().parents[2]
module_path = base_dir / "theory-of-everything-simulations" / "theory_of_everything_app.py"
spec = importlib.util.spec_from_file_location("toe_80_app", module_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod) 