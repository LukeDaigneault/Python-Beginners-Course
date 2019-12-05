from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


message = MIMEMultipart()
message["from"] = "Luke Daigneault"
message["to"] = "luke.daigneault@gmail.com"
message["subject"] = "This is a test"

message.attach(MIMEText("Body"))
message.attach(MIMEImage(Path("image.png").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("luke.daigneault@gmail.com", "password goes here")
    smtp.send_message(message)
    print("Sent....")
