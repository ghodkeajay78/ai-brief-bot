import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

# Function to send an email

def send_email(subject, body, to_email):
    """
    Send an email using SMTP.
    
    :param subject: Subject of the email
    :param body: Body of the email
    :param to_email: Recipient's email address
    """
    try:
        # Email configuration
        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = os.getenv('SMTP_PORT')
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
            print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')  # Error handling

if __name__ == '__main__':
    # Example usage
    send_email('Test Subject', 'This is a test email body.', 'recipient@example.com')
