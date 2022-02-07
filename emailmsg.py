#!/usr/bin/env python3

from smtplib import SMTP
from sys import argv


def main():
    host = input("Enter fqdn or IP address: ")
    port = 587

    username = input("Sender email address: ")
    password = "#test$3372"

    from_email = username
    to_list = input("Recipient email address: ")
    message = input("Message: ")


    CON = SMTP(host,port)
    try:
        CON.ehlo()
        CON.starttls()
        CON.login(username, password)
        CON.sendmail(from_email, to_list, message)
    except:
        print("An error ocurred")

    CON.quit()


if __name__ == '__main__':
    main()

