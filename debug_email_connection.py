
import smtplib
from email.mime.text import MIMEText

def test_smtp_connection():
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "itvadesk@gmail.com"
    # This password was present in the config
    smtp_password = "jdffvrnipwmwtoeb" 

    sender = smtp_user
    recipient = "ritiks.987654321@gmail.com"

    msg = MIMEText("This is a test email from the debugger script.")
    msg['Subject'] = "SMTP Debug Test"
    msg['From'] = sender
    msg['To'] = recipient

    print(f"Attempting to connect to {smtp_server}:{smtp_port}...")
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.set_debuglevel(1)  # Show low-level communication
        print("EHLO...")
        server.ehlo()
        print("STARTTLS...")
        server.starttls()
        print("EHLO...")
        server.ehlo()
        print(f"Logging in as {smtp_user}...")
        server.login(smtp_user, smtp_password)
        print("Login successful!")
        print(f"Sending mail to {recipient}...")
        server.sendmail(sender, recipient, msg.as_string())
        print("Mail sent successfully!")
        server.quit()
    except Exception as e:
        print(f"SMTP FAILED: {e}")

if __name__ == "__main__":
    test_smtp_connection()
