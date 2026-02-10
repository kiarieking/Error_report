import smtplib
from email.message import EmailMessage

sender_email = 'kiariekevin22@gmail.com'
receiver_email = 'kelvin.kiarie@quatrixglobal.com'
app_password = 'zfyu sang zeuc ycvg'

msg =  EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Log Alert: Error Detected in Logs"
msg.set_content("An error has been detected in the logs. Please check the attached log file for details.")
with open("/home/kkiarie/code/logs_notifier/log_notifier.log", "r") as f:
    log_content = f.read()
msg.add_attachment(log_content, filename="error_only.log") 

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent successfully!")
