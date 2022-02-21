
import smtplib

from email.message import EmailMessage

massage = EmailMessage()
massage['Subject'] = 'test it'
massage['From'] = 'salimbader734@gmail.com' # user email address
massage['To'] = 'salimbader18@gmail.com' # to who you want send email

massage.set_content('This is a test email')


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: # 465 is the gmail port number
    smtp.login("salimbader734@gmail.com", "123456SS")# user email address and password
    smtp.send_message(massage)