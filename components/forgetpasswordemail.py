
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

<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
    <title>Forget password</title>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
    <!--[if !mso]><!-->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css" />
    <link href="https://fonts.googleapis.com/css?family=Cabin" rel="stylesheet" type="text/css" />
    <!--<![endif]-->
    <style>
        * {
            box-sizing: border-box;
        }
        
        body {
            margin: 0;
            padding: 0;
        }
        
        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: inherit !important;
        }
        
        #MessageViewBody a {
            color: inherit;
            text-decoration: none;
        }
        
        p {
            line-height: inherit
        }
        
        @media (max-width:620px) {
            .row-content {
                width: 100% !important;
            }
            .image_block img.big {
                width: auto !important;
            }
            .stack .column {
                width: 100%;
                display: block;
            }
        }
    </style>
</head>

<body style="background-color: #d9dffa; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
    <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9dffa;" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #cfd6f4;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 600px;" width="600">
                                        <tbody>
                                            <tr>
                                                <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 20px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div align="center" style="line-height:10px"><img alt="Card Header with Border and Shadow Animated" class="big" src="images/animated_header.gif" style="display: block; height: auto; border: 0; width: 600px; max-width: 100%;" title="Card Header with Border and Shadow Animated"
                                                                        width="600" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #d9dffa; background-image: url('images/body_background_2.png'); background-position: top center; background-repeat: repeat;"
                        width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 600px;" width="600">
                                        <tbody>
                                            <tr>
                                                <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-left: 50px; padding-right: 50px; padding-top: 15px; padding-bottom: 15px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #506bec; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px;"><strong><span style="font-size:38px;">Forgot your password?</span></strong></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #40507a; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px;"><span style="font-size:16px;">Hey, we received a request to reset your password.</span></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #40507a; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px;"><span style="font-size:16px;">Let’s get you a new one!</span></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="button_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:20px;text-align:left;">
                                                                <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="http://www.example.com/" style="height:48px;width:212px;v-text-anchor:middle;" arcsize="34%" stroke="false" fillcolor="#506bec"><w:anchorlock/><v:textbox inset="5px,0px,0px,0px"><center style="color:#ffffff; font-family:Arial, sans-serif; font-size:15px"><![endif]--><a href="http://www.example.com/" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#506bec;border-radius:16px;width:auto;border-top:0px solid TRANSPARENT;border-right:0px solid TRANSPARENT;border-bottom:0px solid TRANSPARENT;border-left:0px solid TRANSPARENT;padding-top:8px;padding-bottom:8px;font-family:Helvetica Neue, Helvetica, Arial, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;"
                                                                    target="_blank"><span style="padding-left:25px;padding-right:20px;font-size:15px;display:inline-block;letter-spacing:normal;"><span style="font-size: 16px; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><span data-mce-style="font-size: 15px; line-height: 30px;" style="font-size: 15px; line-height: 30px;"><strong>RESET MY PASSWORD</strong></span></span></span></a>
                                                                <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #40507a; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px;"><span style="font-size:14px;">Having trouble? <a href="http://www.example.com/" rel="noopener" style="text-decoration: none; color: #40507a;" target="_blank" title="@socialaccount"><strong>@socialaccount</strong></a></span></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #40507a; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px;">Didn’t request a password reset? You can ignore this message.</p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 600px;" width="600">
                                        <tbody>
                                            <tr>
                                                <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td style="width:100%;padding-right:0px;padding-left:0px;">
                                                                <div align="center" style="line-height:10px"><img alt="Card Bottom with Border and Shadow Image" class="big" src="images/bottom_img.png" style="display: block; height: auto; border: 0; width: 600px; max-width: 100%;" title="Card Bottom with Border and Shadow Image"
                                                                        width="600" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 600px;" width="600">
                                        <tbody>
                                            <tr>
                                                <td class="column" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-left: 10px; padding-right: 10px; padding-top: 10px; padding-bottom: 20px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;"
                                                    width="100%">
                                                    <table border="0" cellpadding="10" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div align="center" style="line-height:10px">
                                                                    <a href="http://www.example.com/" style="outline:none" tabindex="-1" target="_blank"><img alt="Your Logo" src="images/DKcubedLogo.png" style="display: block; height: auto; border: 0; width: 145px; max-width: 100%;" title="Your Logo" width="145" /></a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="social_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <table align="center" border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="72px">
                                                                    <tr>
                                                                        <td style="padding:0 2px 0 2px;">
                                                                            <a href="https://www.instagram.com/" target="_blank"><img alt="Instagram" height="32" src="images/instagram2x.png" style="display: block; height: auto; border: 0;" title="instagram" width="32" /></a>
                                                                        </td>
                                                                        <td style="padding:0 2px 0 2px;">
                                                                            <a href="https://www.twitter.com/" target="_blank"><img alt="Twitter" height="32" src="images/twitter2x.png" style="display: block; height: auto; border: 0;" title="twitter" width="32" /></a>
                                                                        </td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #97a2da; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: center;">+(44) 7467759544 </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #97a2da; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: center;">This link will expire in the next 24 hours.<br/>Please feel free to contact us at salim@DKA^3.com.</p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="10" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td>
                                                                <div style="font-family: sans-serif">
                                                                    <div style="font-size: 14px; mso-line-height-alt: 16.8px; color: #97a2da; line-height: 1.2; font-family: Helvetica Neue, Helvetica, Arial, sans-serif;">
                                                                        <p style="margin: 0; text-align: center; font-size: 12px;"><span style="font-size:12px;">Copyright© 2021 DKA^3.</span></p>
                                                                        <p id="m_8010100107078456808text01" style="margin: 0; text-align: center; font-size: 12px;"><span style="font-size:12px;"><a href="http://www.example.com/" rel="noopener" style="text-decoration: underline; color: #97a2da;" target="_blank" title="Unsubscribe ">Unsubscribe</a> | <a href="http://www.example.com/" rel="noopener" style="text-decoration: underline; color: #97a2da;" target="_blank" title="Manage your preferences">Manage your preferences</a> | <a href="http://www.example.com/" rel="noopener" style="text-decoration: underline; color: #97a2da;" target="_blank" title="Privacy Policy">Privacy Policy</a></span></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
    <!-- End -->
</body>

</html>
        """
    
    
To = 'salimbader22@gmail.com'
From = 'salimbader734@gmail.com'

send_mail("Test email", email_content, To, From)