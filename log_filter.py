import re
from pathlib import Path
from email_notification import EmailNotifier
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECIPIENT_EMAIL")
app_password = os.getenv("APP_PASSWORD")

print(f"Sender Email: {sender_email}")
print(f"Receiver Email: {receiver_email}")
print(f"App Password: {app_password}")

LOG_FILE = "/var/log/postgresql/postgresql-17-main.log"
OUTPUT_FILE = "/home/kkiaries/logs_notifier/log_notifier.log"

ERROR_PATTERNS = [

    r"\bERROR\b",
    r"\bstarting PostgreSQL\b",
    r"\bshutting down\b",
    
    ]

def is_error(line: str)->bool:
    for pat in ERROR_PATTERNS:
        if re.search(pat, line, re.IGNORECASE):
            return True
    return False


def filter_errors(log_path:str):
    log_path = Path(log_path)
    today = datetime.utcnow().strftime("%Y-%m-%d")

    if not log_path.exists():
        raise FileNotFoundError(f"{log_path} dos not exist")
    
    try:
        with log_path.open("r", errors="ignore") as log, open(OUTPUT_FILE,"w") as out:
            for line in log:
                if not line.startswith(today):
                    continue
                if is_error(line):
                    out.write(line)
    except FileNotFoundError as e:
        print(f"Error in filepath: {e}")
    except Exception as e:
        print (f"General Error: {e}")


    print(f"Filtered errors Written to to {OUTPUT_FILE}")

    email_notification = EmailNotifier(sender_email=sender_email,app_password=app_password)
    email_notification.send_email(receiver_email=receiver_email,subject="Log Alert: Error Detected in Logs",
    body="An error has been detected in the logs. Please check the attached log file for details."
    ,attachment_path=OUTPUT_FILE)

    print("Email sent successfully!")

if __name__ == "__main__":
    filter_errors(LOG_FILE)