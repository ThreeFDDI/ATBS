#!/usr/local/bin/python3

# Chapter 16 – Sending Email and Text Messages

# ATBS-16.py 

import email, smtplib, ssl

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('MySMS5858', '5232iwEY3mrExC6xbn8k')

smtpObj.sendmail('MySMS5858@gmail.com', 'foosyou@gmail.com', 'Subject: So long.')

#smtpObj.quit()
