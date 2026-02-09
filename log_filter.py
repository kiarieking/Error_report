import re
from pathlib import Path

LOG_FILE = "/var/log/odoo15/odoo15.log"
OUTPUT_FILE = "/home/kkiarie/code/error_report/error_only.log"

ERROR_PATTERNS = [

    r"\bFileNotFoundError\b",
    r"\bCRICTICAL\b",
    r"\bWARNING\b",
]

def is_error(line: str)->bool:
    for pat in ERROR_PATTERNS:
        re.search(pat, line, re.IGNORECASE)


def filter_errors(log_path:str):
    log_path = Path(log_path)

    if not log_path.exists():
        raise FileNotFoundError(f"{log_path} dos not exist")
    
    with log_path.open("r", errors="ignore") as log, open(OUTPUT_FILE,"w") as out:
        for line in log:
            if is_error(line):
                out.write(line)

    print(f"Filtered errors Written to to {OUTPUT_FILE}")

if __name__ == "__main__":
    filter_errors(LOG_FILE)