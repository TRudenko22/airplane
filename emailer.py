from dataclasses import dataclass
from datetime import date
import smtplib
import typer


APP = typer.Typer()


@dataclass
class Email:
    sender: str
    recipient: str
    subject: str
    body: str


@dataclass
class EmailMessage:
    email: Email
    timestamp: str

    def __str__(self):
        return f"{self.timestamp} - {self.email.sender} -> {self.email.recipient}: {self.email.subject}"


@dataclass()
class EmailSender:
    email: Email
    smtp_user: str
    smtp_password: str
    smtp_server: str = "smtp.gmail.com"
    smtp_port: int = 587

    def send(self):
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.sendmail(self.email.sender, self.email.recipient, self.email.body)


@APP.command()
def send_email(recipient: str, subject: str, body: str):
    """Send an email.""" 

    # Hardcoded for now.
    # Later, I'll use a config file or something.
    password = "your_gmail_app_password"
    sender = "Your email"

    email_content = Email(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
    )

    email_sender = EmailSender(
        email=email_content,
        smtp_user=email_content.sender,
        smtp_password=password,
    )

    email_sender.send()
    print(EmailMessage(email_content, date.today()))


if __name__ == "__main__":
    APP()

    
