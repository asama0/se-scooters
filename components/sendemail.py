
import smtplib

from email.message import EmailMessage

massage = EmailMessage()
massage['Subject'] = 'test it'
massage['From'] = 'salimbader734@gmail.com'
massage['To'] = 'salimbader18@gmail.com'

massage.set_content('hi our nice group')


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("salimbader734@gmail.com", "123456SS")
    smtp.send_message(massage)

    
    