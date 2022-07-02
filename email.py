from dataclasses import dataclass
import smtplib


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


#TODO:
# - Add logging
# - Add TOML config file
# - Add Text parsing for email object



