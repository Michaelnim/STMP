import os.path
import mimetypes
import smtplib
import getpass
from email.message import EmailMessage

#Constructor to create email
message = EmailMessage()

#Email for sender and recipient
sender = "some_email@gmail.com"
recipient = "some_email@gmail.com"

#Title of email
message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

#Message of email
body = "Hello, this is my first python message through email"
message.set_content(body)

#Creating varible for the picture being sent
attachment_path = (r"file_path_to_some_picture.jpg/png/gif")
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

#Using the picture varible to send through email
with open(attachment_path, 'rb') as ap:
     message.add_attachment(ap.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=os.path.basename(attachment_path))


#Setting up mail server be sure to enable IMAP and create a new app and use password
mail_server = smtplib.SMTP_SSL('smtp.gmail/yahoo/hotmail.com')
mail_server.set_debuglevel(1)
mail_pass = getpass.getpass("Password? ")
mail_server.login(sender, mail_pass)
mail_server.send_message(message)