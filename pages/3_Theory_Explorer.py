import importlib.util
from pathlib import Path

# Load theory-explorer/app.py
base_dir = Path(__file__).resolve().parents[2]
module_path = base_dir / "theory-explorer" / "app.py"
spec = importlib.util.spec_from_file_location("theory_explorer_app", module_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod) 