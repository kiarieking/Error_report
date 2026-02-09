import re
from pathlib import Path

LOG_FILE = "/var/log/postgresql/postgresql-17-main.log"
OUTPUT_FILE = "/home/kkiarie/error_report/error_only.log"

ERROR_PATTERNS = [

    r"\bERROR\b",
    r"\bSTATEMENT\b",
    
    ]

def is_error(line: str)->bool:
    for pat in ERROR_PATTERNS:
        if re.search(pat, line, re.IGNORECASE):
            return True
    return False


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