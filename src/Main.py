#this is second commit

import psutil
import smtplib
import time

print(psutil.sensors_battery().percent)

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.starttls()

smtpObj.login('frommail@gmail.com','testpswd')

smtpObj.sendmail("frommail@gmail.com","tomail@yandex.ru","Program start!")

while True:
    print("I work")
    time.sleep(5)   # Delay
    if psutil.sensors_battery().percent<99:
        myMassage = "Now battary is less than " + str(psutil.sensors_battery().percent)
        print("I send")