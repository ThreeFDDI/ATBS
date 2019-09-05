#!/usr/local/bin/python3

# Chapter 16 – Sending Email and Text Messages

# ATBS-16.py 

import smtplib

smtpObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)

smtpObj.ehlo()

smtpObj.login('MyEmail@gmail.com', 'notapassword')

smtpObj.sendmail('MyEmail@gmail.com', [ 'YourEmail@gmail.com'], 'Subject: I <3 Python.')

smtpObj.quit()
