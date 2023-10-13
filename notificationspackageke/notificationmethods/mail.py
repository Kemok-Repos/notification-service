from email.message import EmailMessage
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(user, passwd,subject,
              to_addrs,smtp_host='smtp.gmail.com', smtp_port=587,
              reply_to='soporte@kemok.io', attachments=None, bcc=['analyst@kemok.io'],body='<p>--Emtpy--</p>',
              ):
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.ehlo(name='gc.kemok.io')
        server.starttls(context=context)
        server.ehlo(name='gc.kemok.io')
        server.login(user, passwd)

        if isinstance(to_addrs, str):
            to_addrs = [i.strip() for i in to_addrs.split(',') if i.strip()]
        msg = MIMEMultipart()
        msg.attach(MIMEText(body, 'html'))
        msg['Subject'] = subject
        msg['From'] = user
        msg['To'] = ', '.join(to_addrs)
        msg['reply-to'] = reply_to
        to_addrs += bcc
        if attachments:
            for attachment in attachments:
                part = MIMEBase('application', 'octet-stream')
                with open(attachment, 'rb') as f:
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment',
                                filename=attachment.split('/')[-1])
                msg.attach(part)
        server.sendmail(user, to_addrs, msg.as_string())
    except Exception as error:
        print(error)