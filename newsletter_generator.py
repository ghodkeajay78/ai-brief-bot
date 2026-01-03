import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
from dotenv import load_dotenv
load_dotenv()


def generate_newsletter(content):
    """Generates a newsletter with the given content."""
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_FROM')
    msg['To'] = os.getenv('EMAIL_TO')
    msg['Subject'] = 'Your Newsletter'

    # Attach the content
    msg.attach(MIMEText(content, 'html'))

    return msg


def send_newsletter(msg):
    """Sends the newsletter via SMTP."""
    try:
        with smtplib.SMTP(os.getenv('SMTP_SERVER'), os.getenv('SMTP_PORT')) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_FROM'), os.getenv('EMAIL_PASSWORD'))
            server.send_message(msg)
            print('Newsletter sent successfully!')
    except Exception as e:
        print(f'Error sending newsletter: {e}')


if __name__ == '__main__':
    newsletter_content = '<h1>Weekly Update</h1><p>Your content goes here.</p>'
    newsletter = generate_newsletter(newsletter_content)
    send_newsletter(newsletter)
