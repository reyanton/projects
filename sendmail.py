import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'reinaldovillarroel@grupodavid.com'
EMAIL_PASSWORD = '**-r28l20p31-**'

msg = EmailMessage()
msg['Subject'] = 'This is my first Python email'
msg['From'] = EMAIL_ADDRESS 
msg['To'] = 'reinaldo.vanton@gmail.com' 
msg.set_content('''
<!DOCTYPE html>
<html>
    <body>
        <div style="background-color:#eee;padding:10px 20px;">
            <h2 style="font-family:Georgia, 'Times New Roman', Times, serif;color#454349;">My newsletter</h2>
        </div>
        <div style="padding:20px 0px">
            <div style="height: 500px;width:400px">
                <img src="https://dummyimage.com/500x300/000/fff&text=Dummy+image" style="height: 300px;">
                <div style="text-align:center;">
                    <h3>Article 1</h3>
                    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. A ducimus deleniti nemo quibusdam iste sint!</p>
                    <a href="#">Read more</a>
                </div>
            </div>
        </div>
    </body>
</html>
''', subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
    smtp.send_message(msg)