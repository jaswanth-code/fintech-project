import subprocess
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

scripts = [
    "load_all_datasets.py",
    "clean_fund_master.py",
    "clean_investor_transactions.py",
    "clean_nav_history.py",
    "clean_scheme_performance.py",
    "create_database.py"
]

for script in scripts:
    script_path = os.path.join(SCRIPT_DIR, script)

    print(f"Running {script}...")

    subprocess.run(
        ["python", script_path],
        check=True
    )

print("ETL Pipeline Completed Successfully")