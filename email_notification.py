import smtplib
from email.message import EmailMessage

class EmailNotifier:
        def __init__(self,sender_email,app_password):
            self.sender_email = sender_email
            self.app_password = app_password

        def send_email(self,receiver_email,subject,body,attachment_path=None):
            msg = EmailMessage()
            msg["From"] = self.sender_email
            msg["To"] = receiver_email
            msg["Subject"] = subject
            msg.set_content(body)

            try:
                if attachment_path:
                    try:
                        with open(attachment_path,"r") as f:
                            log_content = f.read()
                        msg.add_attachment(log_content, filename="error_only.log")
                    except FileNotFoundError:
                        print(f"Attachment file not found: {attachment_path}")
                        return
                    except Exception as e:
                        print(f"Error reading file: {e}")
                        return

            try:

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                    server.login(self.sender_email, self.app_password)
                    server.send_message(msg)

                print("Email sent successfully!")

                except smtplib.SMTPAuthenticationError:
                    print("Authentication failed. Please check your email and app password.")
                except smtplib.SMTPException as e:
                    print(f"SMTP error occurred: {e}")
                except Exception as e:
                    print(f"An error occurred: {e}")

            except Exception as e:
                print(f"An error occurred while sending email: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


