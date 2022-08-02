import smtplib

message = 'HOla, un mensaje de python'
subject = 'Prueba de correo'

message = 'Subject: {}\n\n{}'.format(subject, message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('soporteqservices@gmail.com','qvqsjjrbiulpndie') #

server.sendmail('soporteqservices@gmail.com',"luen.cg08@gmail.com",message)
server.quit()
print("successfully sent email")

