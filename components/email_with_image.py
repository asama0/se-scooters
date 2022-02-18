from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
import smtplib

def send_mail(Subject, From, To, Body):
    msg = EmailMessage()

    # generic email headers
    msg['Subject'] = Subject
    msg['From'] = From
    msg['To'] = To

    # set the plain text body
    msg.set_content('This is a plain text body.')

    # now create a Content-ID for the image
    image_cid = make_msgid(domain='gmail.com')
    # if `domain` argument isn't provided, it will
    # use your computer's name

    # set an alternative html body
    msg.add_alternative(f"""\
    <html>
        <body>
            <p>This is an HTML body.<br>
            It <i>also</i> has <b>an image<b>.
            </p>
            <img src="cid:{image_cid[1:-1]}">
        </body>
    </html>
    """, subtype='html')
    # image_cid looks like <long.random.number@xyz.com>
    # to use it as the img src, we don't need `<` or `>`
    # so we use [1:-1] to strip them off


    # now open the image and attach it to the email
    with open('email_images/grapefruit.jpeg', 'rb') as img:

        # know the Content-Type of the image
        maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')

        # attach it
        msg.get_payload()[1].add_related(img.read(),
                                            maintype=maintype,
                                            subtype=subtype,
                                            cid=image_cid)

    # the message is ready now
    # you can write it to a file
    # or send it using smtplib

    ser = smtplib.SMTP("smtp.gmail.com:587")
    Password = "123456SS"
    ser.starttls()
    ser.login(msg['From'], Password)
    ser.send_message(msg)
    ser.quit()


def main():
    send_mail('Hello there', 'salimbader734@gmail.com', 'fy19amaa@leeds.ac.uk', '')

if __name__ == '__main__':
    main()
