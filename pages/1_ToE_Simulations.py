import importlib.util
from pathlib import Path

# Load ToE-Simulations/app.py under an alias so its Streamlit UI renders inside this page
base_dir = Path(__file__).resolve().parents[2]
module_path = base_dir / "ToE-Simulations" / "app.py"
spec = importlib.util.spec_from_file_location("toe_simulations_app", module_path)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod) 