
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



def send_mail(Subject, Body, To, From):
    
    massage = MIMEMultipart('alternative')
    massage['Subject'] = Subject
    massage['From'] = To # user email address
    massage['To'] = From # to who you want send email 

#the MIME type text/html
    Html_Body = MIMEText(Body, "html")
# attch the html code to massage container
    massage.attach(Html_Body)
#the port number of gmail.com
    ser = smtplib.SMTP("smtp.gmail.com:587")
#password of the user who want to send email
    Password = "123456SS"

    ser.starttls()
    ser.login(From, Password)
    ser.sendmail(From, [To], massage.as_string())
    ser.quit()
    
if __name__ == "__main__":
    email_content = """
        <!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
    <meta charset="utf-8">
    <title>receipt page</title>

    <style>
        .btn:hover {
            background-color: rgb(90, 88, 88);
            color: #000;
        }
    </style>
</head>

<body style="color: #000;">
    <div class="receipt" style="background-color: rgb(183, 187, 187);
    width: 400px;
    height: 350px;
    position: absolute;
    top: -50px;
    left: 0%;
    margin: 50px auto;
    border: 10px solid #000;">

        <div class="main">
            <div class="nameofapp">
                <h1>NAME OF APP</h1>
            </div>
        </div>
        <h1 style="color: rgb(3, 3, 3);
        width: 300px;">Thanks for renting our scooter, Salim</h1>
        <h2 style="color: rgb(6, 248, 26);
        font-size: 20px;">Here's your receipt from nameofapp (leeds).</h2>
        <div class="button" style=" transform: translate(-50%-50%);
        top: 250px;">
            <a href="Rate.html" class="btn" style="border: 1px solid rgb(12, 11, 11);
            padding: 10px 30px;
            color: rgb(12, 10, 10);
            text-decoration: none;
            transition: 0, 6s ease;">Rate Order</a>
        </div>
        <div class="price" style="position: relative;
        top: 50px;">
            <h1>Total £8.27</h1>
        </div>
    </div>

</body>

</html>
    """
    
    
To = 'salimbader22@gmail.com'
From = 'salimbader734@gmail.com'

send_mail("Test email", email_content, To, From)