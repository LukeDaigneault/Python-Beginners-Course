from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

template = Template(
    Path("./python_standard_library/template.html").read_text())


message = MIMEMultipart()
message["from"] = "Luke Daigneault"
message["to"] = "luke.daigneault@gmail.com"
message["subject"] = "This is a test"

message.attach(MIMEText(template.substitute({"name": "John"}), "html"))
message.attach(MIMEImage(Path("image.png").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("luke.daigneault@gmail.com", "password goes here")
    smtp.send_message(message)
    print("Sent....")
