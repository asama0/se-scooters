
import smtplib


ser = smtplib.SMTP_SSL("smtp.gmail.com", 465)
ser.login("salimbader734@gmail.com", "123456SS")
ser.sendmail("salimbader734@gmail.com", 
             "salimbader22@gmail.com", 
             "hi salim")


ser.quit()


    
    