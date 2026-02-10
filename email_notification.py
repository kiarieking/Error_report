import smtplib
from email.message import EmailMessage

sender_email = 'kiariekevin22@gmail.com;
receiver_email = 'kelvin.kiarie@quatrixglobal.com'
app_password = 'zfyu sang zeuc ycvg'

msg =  EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Log Alert: Error Detected in Logs"
msg.set_content("An error has been detected in the logs. Please check the attached log file for details.")
with open("/home/kkiarie/error_report/error_only.log", "r") as f:
    log_content = f.read()
msg.add_attachment(log_content, filename="error_only.log") 
