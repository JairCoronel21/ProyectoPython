import random
import smtplib
def enviarv2(correo):
    p = random.randint(9999,99999)
    p = str(p)
    message = 'Codigo de seguridad: ' + p
    subject = 'QSERVICES'

    message = 'Subject: {}\n\n{}'.format(subject, message)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('soporteqservices@gmail.com','qvqsjjrbiulpndie') #

    server.sendmail('soporteqservices@gmail.com',correo,message)
    server.quit()
    print("successfully sent email")
    print("Revisar SPAM")
    return p
    

