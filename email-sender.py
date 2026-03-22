import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Final


# It is better ALWAYS load sensitive from an external source that is not located in your project.
EMAIL: Final[str] = '***************'
PASSWORD: Final[str] = '**************'


def create_image_attachment(path: str) -> MIMEImage:

    with open(path, 'rb') as image:
        mime_image = MIMEImage(image.read())
        mime_image.add_header('Content-Disposition', f'attachment; filename={path}')
        return mime_image


def send_email(to_email: str, subject: str, body: str, image: str  = None):
    host: str = "smtp.gmail.com"
    port: int = 587

    context = ssl.create_default_context()

    with smtplib.SMTP(host, port) as server:
        # Login
        print('Logging in...')
        server.ehlo()  # Used to greet the server and identify who we are
        server.starttls(context=context)
        server.ehlo()
        server.login(EMAIL,PASSWORD)  # NEVER INCLUDE SENSITIVE VALUES IN YOUR SCRIPTS!!!

        # Prepare the email
        print('Attempting to send the email...')
        message = MIMEMultipart()
        message['From'] = EMAIL
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # If there is an attachment, attach it to the e-mail
        if image:
            file: MIMEImage = create_image_attachment(image)
            message.attach(file)

        # Send the email
        server.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message.as_string())

        # Success!
        print('Sent!')


if __name__ == '__main__':
    send_email(to_email='****@gmail.com', subject='hello', body='this is a message', image='cat.png')
