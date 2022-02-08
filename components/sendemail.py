
import smtplib

from email.message import EmailMessage

massage = EmailMessage()
massage['Subject'] = 'test it'
massage['From'] = 'salimbader734@gmail.com' # user email address
massage['To'] = 'salimbader18@gmail.com' # to who you want send email 

massage.set_content('hi our nice group')

massage.add_alternative("""\
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
""", subtype='html')




with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp: # 465 is the gmail port number
    smtp.login("salimbader734@gmail.com", "123456SS")# user email address and password
    smtp.send_message(massage)

    
    