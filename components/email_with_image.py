from email.message import EmailMessage
from email.utils import make_msgid
import mimetypes
from os import remove
import smtplib

DOMAIM_NAME = 'google.com'

bodies = {
    'welcome': {
        'filename': 'welcome.html',
        'images': {
            'images/dkcubedlogo.png': make_msgid(domain=DOMAIM_NAME),
            'images/TR.png': make_msgid(domain=DOMAIM_NAME),
            'images/Facebook.png': make_msgid(domain=DOMAIM_NAME),
            'images/Twitter.png': make_msgid(domain=DOMAIM_NAME),
        }
    },
    
    'reciept': {
        'filename': 'reciept.html',
        'images': {
            'images/dkcubedlogo.png': make_msgid(domain=DOMAIM_NAME),
            'images/tick.png': make_msgid(domain=DOMAIM_NAME),
            'images/shop-basket.png': make_msgid(domain=DOMAIM_NAME),
        }
    },
    'forgetpassword': {
            'filename': 'forgot_password.html',
            'images': {
            'images/dkcubedlogo.png': make_msgid(domain=DOMAIM_NAME),
            'images/animated_header.gif': make_msgid(domain=DOMAIM_NAME),
            'images/body_background_2.png': make_msgid(domain=DOMAIM_NAME),
            'images/bottom_img.png': make_msgid(domain=DOMAIM_NAME),
            'images/instagram2x.png': make_msgid(domain=DOMAIM_NAME),
            'images/twitter2x.png': make_msgid(domain=DOMAIM_NAME),
        }
    }
}

def send_mail(Subject, To, Body_name, **kwargs):
    global bodies
    msg = EmailMessage()

    # generic email headers
    msg['Subject'] = Subject
    msg['From'] = 'dkacubed@gmail.com'
    msg['To'] = To

    # set the plain text body
    msg.set_content('This is a plain text body.')

    # now create a Content-ID for the image
    #image_cid = make_msgid(domain='gmail.com')
    # if `domain` argument isn't provided, it will
    # use your computer's name
    with open (bodies[Body_name]['filename'], "r", encoding='utf8') as htmlfile:
        htmlBody = htmlfile.read().replace("\n", "")
        htmlBody = ' '.join(htmlBody.split())

        for key in kwargs.keys():
            htmlBody = htmlBody.replace("{{"+str(key)+"}}", kwargs[key])


    # set an alternative html body
    for image_path, image_cid in bodies[Body_name]['images'].items():
        htmlBody = htmlBody.replace(image_path, image_cid[1:-1])

    # image_cid looks like <long.random.number@xyz.com>
    # to use it as the img src, we don't need `<` or `>`
    # so we use [1:-1] to strip them off

    msg.add_alternative(htmlBody, subtype='html')


    # now open the image and attach it to the email
    for image_path, image_cid in bodies[Body_name]['images'].items():
        with open(image_path, 'rb') as img:

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
    Password = "RX52@h@MqMj3"
    ser.starttls()
    ser.login(msg['From'], Password)
    ser.send_message(msg)
    ser.quit()


def main():
    send_mail('Hello there', 'salimbader22@gmail.com', 'welcome')
    #send_mail('Hello there', 'salimbader22@gmail.com', 'forgetpassword', forgot_password_url="www.youtube.com")

if __name__ == '__main__':
    main()
