import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEImage import MIMEImage

msg = MIMEMultipart('related')
msg['Subject'] = "My text dated %s" % (today)
msg['From'] = sender
msg['To'] = receiver

html = """\
<html>
  <head></head>
    <body>
      <img src="cid:image1" alt="Logo" style="width:250px;height:50px;"><br>
       <p><h4 style="font-size:15px;">Some Text.</h4></p>           
    </body>
</html>
"""
# Record the MIME types of text/html.
part2 = MIMEText(html, 'html')

# Attach parts into message container.
msg.attach(part2)

# This example assumes the image is in the current directory
fp = open('logo.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# Send the message via local SMTP server.
mailsrv = smtplib.SMTP('localhost')
mailsrv.sendmail(sender, receiver, msg.as_string())
mailsrv.quit()