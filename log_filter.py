import re
from pathlib import Path
from email_notification import EmailNotifier

LOG_FILE = "/var/log/postgresql/postgresql-17-main.log"
OUTPUT_FILE = "/home/kkiarie/logs_notifier/log_notifier.log"

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

    email_notification = EmailNotifier(sender_email="kiariekevin22@gmail.com",app_password="zfyu sang zeuc ycvg")
    email_notification.send_email(receiver_email="kelvin.kiarie@quatrixglobal.com",subject="Log Alert: Error Detected in Logs",
    body="An error has been detected in the logs. Please check the attached log file for details."
    ,attachment_path=OUTPUT_FILE)

    print("Email sent successfully!")

if __name__ == "__main__":
    filter_errors(LOG_FILE)