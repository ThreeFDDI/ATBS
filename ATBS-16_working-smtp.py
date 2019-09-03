import smtplib

gmail_user = 'user@gmail.com'
gmail_password = 'homy password goes here'

sent_from = gmail_user
to = [ '5745140029@vtext.com']
subject = 'Check your server script - it exited'
body = 'Will put a variable here later.'

email_text = """\
From: %s
To: %s
Subject: %s

%s

""" % (sent_from, ", ".join(to), subject, body)

try:
     server=smtplib.SMTP_SSL('smtp.gmail.com', 465)
     server.ehlo()
     server.login(gmail_user, gmail_password)
     server.sendmail(sent_from, to, email_text)
     server.close()

except:
         print('Something went wrong')