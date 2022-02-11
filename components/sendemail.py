
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
        <!doctype html>
<html ⚡4email data-css-strict>

<head>
    <meta charset="utf-8">
    <style amp4email-boilerplate>
        body {
            visibility: hidden
        }
    </style>
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <style amp-custom>
        .es-desk-hidden {
            display: none;
            float: left;
            overflow: hidden;
            width: 0;
            max-height: 0;
            line-height: 0;
        }
        
        s {
            text-decoration: line-through;
        }
        
        body {
            width: 100%;
            font-family: "open sans", "helvetica neue", helvetica, arial, sans-serif;
        }
        
        table {
            border-collapse: collapse;
            border-spacing: 0px;
        }
        
        table td,
        html,
        body,
        .es-wrapper {
            padding: 0;
            Margin: 0;
        }
        
        .es-content,
        .es-header,
        .es-footer {
            table-layout: fixed;
            width: 100%;
        }
        
        p,
        hr {
            Margin: 0;
        }
        
        h1,
        h2,
        h3,
        h4,
        h5 {
            Margin: 0;
            line-height: 120%;
            font-family: "open sans", "helvetica neue", helvetica, arial, sans-serif;
        }
        
        .es-left {
            float: left;
        }
        
        .es-right {
            float: right;
        }
        
        .es-p5 {
            padding: 5px;
        }
        
        .es-p5t {
            padding-top: 5px;
        }
        
        .es-p5b {
            padding-bottom: 5px;
        }
        
        .es-p5l {
            padding-left: 5px;
        }
        
        .es-p5r {
            padding-right: 5px;
        }
        
        .es-p10 {
            padding: 10px;
        }
        
        .es-p10t {
            padding-top: 10px;
        }
        
        .es-p10b {
            padding-bottom: 10px;
        }
        
        .es-p10l {
            padding-left: 10px;
        }
        
        .es-p10r {
            padding-right: 10px;
        }
        
        .es-p15 {
            padding: 15px;
        }
        
        .es-p15t {
            padding-top: 15px;
        }
        
        .es-p15b {
            padding-bottom: 15px;
        }
        
        .es-p15l {
            padding-left: 15px;
        }
        
        .es-p15r {
            padding-right: 15px;
        }
        
        .es-p20 {
            padding: 20px;
        }
        
        .es-p20t {
            padding-top: 20px;
        }
        
        .es-p20b {
            padding-bottom: 20px;
        }
        
        .es-p20l {
            padding-left: 20px;
        }
        
        .es-p20r {
            padding-right: 20px;
        }
        
        .es-p25 {
            padding: 25px;
        }
        
        .es-p25t {
            padding-top: 25px;
        }
        
        .es-p25b {
            padding-bottom: 25px;
        }
        
        .es-p25l {
            padding-left: 25px;
        }
        
        .es-p25r {
            padding-right: 25px;
        }
        
        .es-p30 {
            padding: 30px;
        }
        
        .es-p30t {
            padding-top: 30px;
        }
        
        .es-p30b {
            padding-bottom: 30px;
        }
        
        .es-p30l {
            padding-left: 30px;
        }
        
        .es-p30r {
            padding-right: 30px;
        }
        
        .es-p35 {
            padding: 35px;
        }
        
        .es-p35t {
            padding-top: 35px;
        }
        
        .es-p35b {
            padding-bottom: 35px;
        }
        
        .es-p35l {
            padding-left: 35px;
        }
        
        .es-p35r {
            padding-right: 35px;
        }
        
        .es-p40 {
            padding: 40px;
        }
        
        .es-p40t {
            padding-top: 40px;
        }
        
        .es-p40b {
            padding-bottom: 40px;
        }
        
        .es-p40l {
            padding-left: 40px;
        }
        
        .es-p40r {
            padding-right: 40px;
        }
        
        .es-menu td {
            border: 0;
        }
        
        a {
            text-decoration: none;
        }
        
        p,
        ul li,
        ol li {
            font-family: "open sans", "helvetica neue", helvetica, arial, sans-serif;
            line-height: 150%;
        }
        
        ul li,
        ol li {
            Margin-bottom: 15px;
        }
        
        .es-menu td a {
            text-decoration: none;
            display: block;
            font-family: "open sans", "helvetica neue", helvetica, arial, sans-serif;
        }
        
        .es-menu amp-img,
        .es-button amp-img {
            vertical-align: middle;
        }
        
        .es-wrapper {
            width: 100%;
            height: 100%;
        }
        
        .es-wrapper-color {
            background-color: #EEEEEE;
        }
        
        .es-header {
            background-color: transparent;
        }
        
        .es-header-body {
            background-color: #044767;
        }
        
        .es-header-body p,
        .es-header-body ul li,
        .es-header-body ol li {
            color: #FFFFFF;
            font-size: 14px;
        }
        
        .es-header-body a {
            color: #FFFFFF;
            font-size: 14px;
        }
        
        .es-content-body {
            background-color: #FFFFFF;
        }
        
        .es-content-body p,
        .es-content-body ul li,
        .es-content-body ol li {
            color: #333333;
            font-size: 16px;
        }
        
        .es-content-body a {
            color: #ED8E20;
            font-size: 16px;
        }
        
        .es-footer {
            background-color: transparent;
        }
        
        .es-footer-body {
            background-color: #FFFFFF;
        }
        
        .es-footer-body p,
        .es-footer-body ul li,
        .es-footer-body ol li {
            color: #333333;
            font-size: 14px;
        }
        
        .es-footer-body a {
            color: #333333;
            font-size: 14px;
        }
        
        .es-infoblock,
        .es-infoblock p,
        .es-infoblock ul li,
        .es-infoblock ol li {
            line-height: 120%;
            font-size: 12px;
            color: #CCCCCC;
        }
        
        .es-infoblock a {
            font-size: 12px;
            color: #CCCCCC;
        }
        
        h1 {
            font-size: 36px;
            font-style: normal;
            font-weight: bold;
            color: #333333;
        }
        
        h2 {
            font-size: 30px;
            font-style: normal;
            font-weight: bold;
            color: #333333;
        }
        
        h3 {
            font-size: 18px;
            font-style: normal;
            font-weight: normal;
            color: #333333;
        }
        
        .es-header-body h1 a,
        .es-content-body h1 a,
        .es-footer-body h1 a {
            font-size: 36px;
        }
        
        .es-header-body h2 a,
        .es-content-body h2 a,
        .es-footer-body h2 a {
            font-size: 30px;
        }
        
        .es-header-body h3 a,
        .es-content-body h3 a,
        .es-footer-body h3 a {
            font-size: 18px;
        }
        
        a.es-button,
        button.es-button {
            border-style: solid;
            border-color: #66B3B7;
            border-width: 15px 30px 15px 30px;
            display: inline-block;
            background: #66B3B7;
            border-radius: 5px;
            font-size: 18px;
            font-family: "open sans", "helvetica neue", helvetica, arial, sans-serif;
            font-weight: normal;
            font-style: normal;
            line-height: 120%;
            color: #FFFFFF;
            text-decoration: none;
            width: auto;
            text-align: center;
        }
        
        .es-button-border {
            border-style: solid solid solid solid;
            border-color: transparent transparent transparent transparent;
            background: #66B3B7;
            border-width: 0px 0px 0px 0px;
            display: inline-block;
            border-radius: 5px;
            width: auto;
        }
        
        .es-p-default {
            padding-top: 20px;
            padding-right: 35px;
            padding-bottom: 0px;
            padding-left: 35px;
        }
        
        .es-p-all-default {
            padding: 0px;
        }
        
        @media only screen and (max-width:600px) {
            p,
            ul li,
            ol li,
            a {
                line-height: 150%
            }
            h1,
            h2,
            h3,
            h1 a,
            h2 a,
            h3 a {
                line-height: 120%
            }
            h1 {
                font-size: 32px;
                text-align: center
            }
            h2 {
                font-size: 26px;
                text-align: center
            }
            h3 {
                font-size: 20px;
                text-align: center
            }
            .es-header-body h1 a,
            .es-content-body h1 a,
            .es-footer-body h1 a {
                font-size: 32px
            }
            .es-header-body h2 a,
            .es-content-body h2 a,
            .es-footer-body h2 a {
                font-size: 26px
            }
            .es-header-body h3 a,
            .es-content-body h3 a,
            .es-footer-body h3 a {
                font-size: 20px
            }
            .es-menu td a {
                font-size: 16px
            }
            .es-header-body p,
            .es-header-body ul li,
            .es-header-body ol li,
            .es-header-body a {
                font-size: 16px
            }
            .es-content-body p,
            .es-content-body ul li,
            .es-content-body ol li,
            .es-content-body a {
                font-size: 16px
            }
            .es-footer-body p,
            .es-footer-body ul li,
            .es-footer-body ol li,
            .es-footer-body a {
                font-size: 16px
            }
            .es-infoblock p,
            .es-infoblock ul li,
            .es-infoblock ol li,
            .es-infoblock a {
                font-size: 12px
            }
            *[class="gmail-fix"] {
                display: none
            }
            .es-m-txt-c,
            .es-m-txt-c h1,
            .es-m-txt-c h2,
            .es-m-txt-c h3 {
                text-align: center
            }
            .es-m-txt-r,
            .es-m-txt-r h1,
            .es-m-txt-r h2,
            .es-m-txt-r h3 {
                text-align: right
            }
            .es-m-txt-l,
            .es-m-txt-l h1,
            .es-m-txt-l h2,
            .es-m-txt-l h3 {
                text-align: left
            }
            .es-m-txt-r amp-img {
                float: right
            }
            .es-m-txt-c amp-img {
                margin: 0 auto
            }
            .es-m-txt-l amp-img {
                float: left
            }
            .es-button-border {
                display: inline-block
            }
            a.es-button,
            button.es-button {
                font-size: 16px;
                display: inline-block
            }
            .es-btn-fw {
                border-width: 10px 0px;
                text-align: center
            }
            .es-adaptive table,
            .es-btn-fw,
            .es-btn-fw-brdr,
            .es-left,
            .es-right {
                width: 100%
            }
            .es-content table,
            .es-header table,
            .es-footer table,
            .es-content,
            .es-footer,
            .es-header {
                width: 100%;
                max-width: 600px
            }
            .es-adapt-td {
                display: block;
                width: 100%
            }
            .adapt-img {
                width: 100%;
                height: auto
            }
            td.es-m-p0 {
                padding: 0px
            }
            td.es-m-p0r {
                padding-right: 0px
            }
            td.es-m-p0l {
                padding-left: 0px
            }
            td.es-m-p0t {
                padding-top: 0px
            }
            td.es-m-p0b {
                padding-bottom: 0
            }
            td.es-m-p20b {
                padding-bottom: 20px
            }
            .es-mobile-hidden,
            .es-hidden {
                display: none
            }
            tr.es-desk-hidden,
            td.es-desk-hidden,
            table.es-desk-hidden {
                width: auto;
                overflow: visible;
                float: none;
                max-height: inherit;
                line-height: inherit
            }
            tr.es-desk-hidden {
                display: table-row
            }
            table.es-desk-hidden {
                display: table
            }
            td.es-desk-menu-hidden {
                display: table-cell
            }
            .es-menu td {
                width: 1%
            }
            table.es-table-not-adapt,
            .esd-block-html table {
                width: auto
            }
            table.es-social {
                display: inline-block
            }
            table.es-social td {
                display: inline-block
            }
        }
    </style>
</head>

<body>
    <div class="es-wrapper-color">
        <!--[if gte mso 9]><v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#eeeeee"></v:fill> </v:background><![endif]-->
        <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0">
            <tr>
                <td valign="top">
                    <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                        <tr></tr>
                        <tr>
                            <td align="center">
                                <table class="es-header-body" style="background-color: #044767" width="600" cellspacing="0" cellpadding="0" bgcolor="#044767" align="center">
                                    <tr>
                                        <td class="es-p35t es-p35b es-p35r es-p35l" align="left">
                                            <!--[if mso]><table width="530" cellpadding="0" cellspacing="0"><tr><td width="340" valign="top"><![endif]-->
                                            <table class="es-left" cellspacing="0" cellpadding="0" align="left">
                                                <tr>
                                                    <td class="es-m-p0r es-m-p20b" width="340" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-m-txt-c" align="left">
                                                                    <h1 style="color: #ffffff;line-height: 100%">DKA^3</h1>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                            <!--[if mso]></td><td width="20"></td><td width="170" valign="top"><![endif]-->
                                            <table cellspacing="0" cellpadding="0" align="right">
                                                <tr class="es-hidden">
                                                    <td class="es-m-p20b" width="170" align="left">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p5b" align="center" style="font-size:0">
                                                                    <table width="100%" cellspacing="0" cellpadding="0" border="0" role="presentation">
                                                                        <tr>
                                                                            <td style="border-bottom: 1px solid #044767;background: rgba(0, 0, 0, 0) none repeat scroll 0% 0%;height: 1px;width: 100%;margin: 0px"></td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td>
                                                                    <table cellspacing="0" cellpadding="0" align="right" role="presentation">
                                                                        <tr>
                                                                            <td align="left">
                                                                                <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                                                    <tr>
                                                                                        <td align="right">
                                                                                            <p>Rent</p>
                                                                                        </td>
                                                                                    </tr>
                                                                                </table>
                                                                            </td>
                                                                            <td class="es-p10l" valign="top" align="left" style="font-size:0">
                                                                                <amp-img src="images/77981522050090360.png" alt style="display: block" width="27" height="23"></amp-img>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                            <!--[if mso]></td></tr></table><![endif]-->
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                        <tr>
                            <td align="center">
                                <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                    <tr>
                                        <td class="es-p40t es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p25t es-p25b es-p35r es-p35l" align="center" style="font-size:0">
                                                                    <a target="_blank" href="https://viewstripo.email/">
                                                                        <amp-img src="images/67611522142640957.png" alt style="display: block" width="120" height="115"></amp-img>
                                                                    </a>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="es-p10b" align="center">
                                                                    <h2>Thank You For&nbsp;Renting<br>our scooter!</h2>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="es-p15t es-p20b" align="left">
                                                                    <p style="font-size: 16px;color: #777777">Here's your receipt from&nbsp;DKA^3 (Leeds)</p>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                        <tr>
                            <td align="center">
                                <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center">
                                    <tr>
                                        <td class="es-p20t es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p10t es-p10b es-p10r es-p10l" bgcolor="#eeeeee" align="left">
                                                                    <table style="width: 500px" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left" role="presentation">
                                                                        <tr>
                                                                            <td width="80%">
                                                                                <h4 style="font-size: 18px">Rent Confirmation #</h4>
                                                                            </td>
                                                                            <td width="20%">
                                                                                <h4>2345678</h4>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p10t es-p10b es-p10r es-p10l" align="left">
                                                                    <table style="width: 500px" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left" role="presentation">
                                                                        <tr>
                                                                            <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                <p>Rent Cost</p>
                                                                            </td>
                                                                            <td style="padding: 5px 0" width="20%" align="left">
                                                                                <p>£5</p>
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                <p>Rent Time</p>
                                                                            </td>
                                                                            <td style="padding: 5px 0" width="20%" align="left">
                                                                                <p>30mins</p>
                                                                            </td>
                                                                        </tr>
                                                                        <tr>
                                                                            <td style="padding: 5px 10px 5px 0" width="80%" align="left">
                                                                                <p>Discount</p>
                                                                            </td>
                                                                            <td style="padding: 5px 0" width="20%" align="left">
                                                                                <p>£1</p>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="es-p10t es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table style="border-top: 3px solid #eeeeee;border-bottom: 3px solid #eeeeee" width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p15t es-p15b es-p10r es-p10l" align="left">
                                                                    <table style="width: 500px" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left" role="presentation">
                                                                        <tr>
                                                                            <td width="80%">
                                                                                <h4>TOTAL</h4>
                                                                            </td>
                                                                            <td width="20%">
                                                                                <h4>£4</h4>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="es-p20t es-p35r es-p35l" align="left">
                                            <table cellpadding="0" cellspacing="0" width="100%">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p10t es-p10b es-p10r es-p10l" bgcolor="#eeeeee" align="left">
                                                                    <table style="width: 500px" class="cke_show_border" cellspacing="1" cellpadding="1" border="0" align="left" role="presentation">
                                                                        <tr>
                                                                            <td width="80%">
                                                                                <h4 style="font-size: 18px">Date Of Rent:</h4>
                                                                            </td>
                                                                            <td width="20%">
                                                                                <h4>09/02/2022</h4>
                                                                            </td>
                                                                        </tr>
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <table class="es-content" cellspacing="0" cellpadding="0" align="center">
                        <tr>
                            <td align="center">
                                <table class="es-content-body" style="background-color: #1b9ba3" width="600" cellspacing="0" cellpadding="0" bgcolor="#1b9ba3" align="center">
                                    <tr>
                                        <td class="es-p35t es-p35b es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p25t" align="center">
                                                                    <h2 style="color: #ffffff;font-size: 24px">Get 10% off your next rent.</h2>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="es-p30t es-p15b es-p10r es-p10l" align="center"><span class="es-button-border"><a href="" class="es-button" target="_blank">Awesome</a></span></td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    <table cellpadding="0" cellspacing="0" class="es-footer" align="center">
                        <tr>
                            <td align="center">
                                <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" align="center">
                                    <tr>
                                        <td class="es-p35t es-p40b es-p35r es-p35l" align="left">
                                            <table width="100%" cellspacing="0" cellpadding="0">
                                                <tr>
                                                    <td width="530" valign="top" align="center">
                                                        <table width="100%" cellspacing="0" cellpadding="0" role="presentation">
                                                            <tr>
                                                                <td class="es-p15b" align="center" style="font-size:0">
                                                                    <amp-img src="images/12331522050090454.png" alt="Beretun logo" style="display: block" title="Beretun logo" width="37" height="37"></amp-img>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td class="es-p35b" align="center">
                                                                    <p><b>16 Blenheim Terrace</b></p>
                                                                    <p><strong>Leeds, LS2 9HN</strong></p>
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td align="left" class="es-m-txt-c es-p5b">
                                                                    <p style="color: #777777">If you didn't create an account using this email address, please ignore this email or&nbsp;<u><a target="_blank" style="color: #777777" class="unsubscribe" href="">unsubscribe</a></u>.</p>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </div>
</body>

</html>
        """
    
    
To = 'salimbader22@gmail.com'
From = 'salimbader734@gmail.com'

send_mail("Test email", email_content, To, From)