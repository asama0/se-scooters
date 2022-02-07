
import smtplib

from email.message import EmailMessage

massage = EmailMessage()
massage['Subject'] = 'test it'
massage['From'] = 'salimbader734@gmail.com' # user email address
massage['To'] = 'salimbader18@gmail.com' # to who you want send email 

massage.set_content('hi our nice group')

msg.add_alternative("""\
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <header>
      <div class="main">
        <div class="nameofapp">
          <h1>NAME OF APP</h1>
        </div>
      </div>
    </header>
    <main>
        <div class="title">
            <h1>Thanks for renting our scooter, Salim</h1>
            <h2>Here's your receipt from nameofapp (leeds).</h2>
        </div>
        <div class="button">
            <a href="Rate.html" class="btn">Rate Order</a>
        </div>
    </main> 
    
  </body>
</html>

""", subtype='html')


with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: # 465 is the gmail port number
    smtp.login("salimbader734@gmail.com", "123456SS")# user email address and password
    smtp.send_message(massage)

    
    