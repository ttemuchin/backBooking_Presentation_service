import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_message(text):
    msg = MIMEMultipart()

    receiver = text[0]
    message = f"Уважаемый {text[1]}! Вы записаны на день {text[2]}"

    msg.attach(MIMEText(message, 'plain'))
    msg["Subject"] = "Информация о вашем бронировании"

    server = smtplib.SMTP('smtp.mail.ru: 25')
    server.starttls()
    sender = "blatata2002@bk.ru"
    password = "NWeSgN9Ebz5hGPirus7P"
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()