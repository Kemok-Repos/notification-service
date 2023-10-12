from email.message import EmailMessage
import smtplib

def send_mail(template, sender, sender_psw,subject,to):
    try:
        email = EmailMessage()
        email["From"] = sender
        email["To"] = to
        email["Subject"] = subject
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(sender, sender_psw)
        smtp.sendmail(sender, to, email.as_string())
        smtp.quit()
        print('Email enviado a ', to)
    except Exception as error:
        print(error)