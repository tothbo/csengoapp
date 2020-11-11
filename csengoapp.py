from win10toast import ToastNotifier
import time
import datetime
from time import strftime
import schedule
from playsound import playsound
import calendar
import os.path

toaster = ToastNotifier()

file = open('timetable.txt', 'r')
times = file.readlines()
adatbazis = []

for x in times:
    a = x.rstrip("\n")
    adatbazis.append(a)

print(a)

def csongo(beki):
    if(os.path.exists("kicsongo.mp3") == True or os.path.exists("becsongo.mp3") == True):
        if(beki == 1):
            playsound("becsongo.mp3")
        elif(beki == 2):
            playsound("kicsongo.mp3")
    else:
        print("becsongo.mp3 or kicsongo.mp3 is missing...")


def task(oraszam):
    print("Ertesites es hang kuldese folyamatban...")
    if(oraszam == 0):
        toaster.show_toast("🔔 ➡ 1.", "A pontos idő: 7:45")
        csongo(1)
        print("Siker!")
    elif(oraszam == 1):
        toaster.show_toast("1. ➡ 📕", "A pontos idő: 8:25")
        csongo(2)
        print("Siker!")
    elif(oraszam == 2):
        toaster.show_toast("🔔 ➡ 2.", "A pontos idő: 8:40")
        csongo(1)
        print("Siker!")
    elif(oraszam == 3):
        toaster.show_toast("2. ➡ 📕", "A pontos idő: 9:20")
        csongo(2)
        print("Siker!")
    elif(oraszam == 4):
        toaster.show_toast("🔔 ➡ 3.", "A pontos idő: 9:35")
        csongo(1)
        print("Siker!")
    elif(oraszam == 5):
        toaster.show_toast("3. ➡ 📕", "A pontos idő: 10:15")
        csongo(2)
        print("Siker!")
    elif(oraszam == 6):
        toaster.show_toast("🔔 ➡ 4.", "A pontos idő: 10:30")
        csongo(1)
        print("Siker!")
    elif(oraszam == 7):
        toaster.show_toast("4. ➡ 📕", "A pontos idő: 11:10")
        csongo(2)
        print("Siker!")
    elif(oraszam == 8):
        toaster.show_toast("🔔 ➡ 5.", "A pontos idő: 11:25")
        csongo(1)
        print("Siker!")
    elif(oraszam == 9):
        toaster.show_toast("5. ➡ 📕", "A pontos idő: 12:05")
        csongo(2)
        print("Siker!")
    elif(oraszam == 10):
        toaster.show_toast("🔔 ➡ 6.", "A pontos idő: 12:30")
        csongo(1)
        print("Siker!")
    elif(oraszam == 11):
        toaster.show_toast("6. ➡ 📕", "A pontos idő: 13:10")
        csongo(2)
        print("Siker!")
    elif(oraszam == 12):
        toaster.show_toast("🔔 ➡ 7.", "A pontos idő: 13:25")
        csongo(1)
        print("Siker!")
    elif(oraszam == 13):
        toaster.show_toast("7. ➡ 📕", "A pontos idő: 14:05")
        csongo(2)
        print("Siker!")
    elif(oraszam == 14):
        toaster.show_toast("🔔 ➡ 8.", "A pontos idő: 14:20")
        csongo(1)
        print("Siker!")
    elif(oraszam == 15):
        toaster.show_toast("8. ➡ 📕", "A pontos idő: 15:00")
        csongo(2)
        print("Siker!")
        exit()
    else:
        schedule.clear('ertesites')


def main():
    x = datetime.datetime.now()
    csengo_start = "A csengő app mostantól aktív!"
    print("Started")
    print("List of scheduled jobs:")
    if(calendar.weekday(x.year, x.month, x.day) >= 5):
        toaster.show_toast(
            "Ma nincsenek órák!", "Élvezd a hétvége nyugalmát :)", duration=5, threaded=True)
        runtime = False
    elif(strftime("%H:%M") >= "15:06"):
        toaster.show_toast(
            "Ma nincs több órád!", "Élvezd a délután nyugalmát :)", duration=5, threaded=True)
        runtime = False
    else:
        runtime = True
        toaster.show_toast("Csengő", csengo_start, duration=5, threaded=True)

    # Beütemezés
    for i, ido in enumerate(["07:45", "08:25", "08:40", "09:20", "09:35", "10:15", "10:30", "11:10", "11:25", "12:05", "12:30", "13:10", "13:25", "14:05", "14:20", "15:00"]):
        schedule.every().day.at(ido).do(task, oraszam=i).tag('ertesites')
        
    while runtime == True:
        schedule.run_pending()
        time.sleep(1)

    print("Everything done! Shutting down...")


if __name__ == "__main__":
    main()
