import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_addr = 'dummyname20.05@gmail.com'
    to_addr = 'yaswanthalapati20@gmail.com'
    subject = 'Finance Stock Report'

    msg = MIMEMultipart()

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    body = "<b>Today's Finance Stock Report</b>"

    msg.attach(MIMEText(body,'html'))
    my_file = open(filename,'rb')

    part = MIMEBase('applicatinon','octet-stream')
    part.set_payload(my_file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= ' + filename)
    msg.attach(part)

    message = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('dummyname20.05@gmail.com','vjtfweuzmgvxmxlo')


    server.sendmail(from_addr,to_addr,message)

    server.quit()