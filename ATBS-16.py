#!/usr/local/bin/python3

# Chapter 16 – Sending Email and Text Messages

# ATBS-16.py 

import smtplib

smtpObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)

smtpObj.ehlo()

smtpObj.login('MySMS5858@gmail.com', 'notapassword')

smtpObj.sendmail('MySMS@gmail.com', [ 'myemail@gmail.com'], 'Subject: I <3 Python.')

smtpObj.quit()
