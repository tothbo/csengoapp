from win10toast import ToastNotifier
import time
import datetime
from time import strftime
import schedule
from playsound import playsound

toaster = ToastNotifier()
csengo_start = "A csengő app mostantól aktív!"
print("Started")
print("List of scheduled jobs:")
toaster.show_toast("Csengő", csengo_start, duration=5, threaded=True)

def task(oraszam):
    print("Ertesites es hang kuldese folyamatban...")
    if(oraszam == 1):
        toaster.show_toast("🔔 ➡ 1.","A pontos idő: 7:45")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 2):
        toaster.show_toast("1. ➡ 📕","A pontos idő: 8:30")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 3):
        toaster.show_toast("🔔 ➡ 2.","A pontos idő: 8:40")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 4):
        toaster.show_toast("2. ➡ 📕","A pontos idő: 9:25")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 5):
        toaster.show_toast("🔔 ➡ 3.","A pontos idő: 9:35")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 6):
        toaster.show_toast("3. ➡ 📕","A pontos idő: 10:20")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 7):
        toaster.show_toast("🔔 ➡ 4.","A pontos idő: 10:30")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 8):
        toaster.show_toast("4. ➡ 📕","A pontos idő: 11:15")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 9):
        toaster.show_toast("🔔 ➡ 5.","A pontos idő: 11:25")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 10):
        toaster.show_toast("5. ➡ 📕","A pontos idő: 12:10")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 11):
        toaster.show_toast("🔔 ➡ 6.","A pontos idő: 12:30")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 12):
        toaster.show_toast("6. ➡ 📕","A pontos idő: 13:15")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 13):
        toaster.show_toast("🔔 ➡ 7.","A pontos idő: 13:25")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 14):
        toaster.show_toast("7. ➡ 📕","A pontos idő: 14:10")
        playsound('kicsongo.mp3')
        print("Siker!")
    elif(oraszam == 15):
        toaster.show_toast("🔔 ➡ 8.","A pontos idő: 14:20")
        playsound('becsongo.mp3')
        print("Siker!")
    elif(oraszam == 16):
        toaster.show_toast("8. ➡ 📕","A pontos idő: 15:05")
        playsound('kicsongo.mp3')
        print("Siker!")
    else:
        toaster.show_toast("?. ➡ 📕","Itt valami hiba történt :/")

schedule.every().day.at("07:45").do(task, 1)
schedule.every().day.at("08:30").do(task, 2)
schedule.every().day.at("08:40").do(task, 3)
schedule.every().day.at("09:25").do(task, 4)
schedule.every().day.at("09:35").do(task, 5)
schedule.every().day.at("10:20").do(task, 6)
schedule.every().day.at("10:30").do(task, 7)
schedule.every().day.at("11:15").do(task, 8)
schedule.every().day.at("11:25").do(task, 9)
schedule.every().day.at("12:10").do(task, 10)
schedule.every().day.at("12:46").do(task, 11)
schedule.every().day.at("13:15").do(task, 12)
schedule.every().day.at("13:25").do(task, 13)
schedule.every().day.at("14:10").do(task, 14)
schedule.every().day.at("14:20").do(task, 15)
schedule.every().day.at("15:05").do(task, 16)

print(schedule.jobs)

while True:
    schedule.run_pending()
    time.sleep(1)