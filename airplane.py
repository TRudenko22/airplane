import email
import typer


app = typer.Typer()


@app.command()
def send_email(sender: str, recipient: str, subject: str, body: str):
    """Send an email.""" 

    # Hardcoded for now.
    # Later, I'll use a config file or something.
    password = "password"

    email_content = email.Email(
        sender=sender,
        recipient=recipient,
        subject=subject,
        body=body,
    )

    email_sender = email.EmailSender(
        email=email_content,
        smtp_user=email_content.sender,
        smtp_password=password,
    )

    email_sender.send()


if __name__ == "__main__":
    app()
    

    
