from plyer import notification
import time
import datetime
from time import strftime
import schedule
from playsound import playsound
import calendar
import os.path
import sys

file = open('timetable.txt', 'r')
times = file.readlines()
adatbazis = []

for x in times:
    a = x.rstrip("\n")
    adatbazis.append(a)

print(adatbazis)

def csongo(beki):
    if(os.path.exists("kicsongo.mp3") == True or os.path.exists("becsongo.mp3") == True):
        if(beki == 1):
            playsound("becsongo.mp3")
        elif(beki == 2):
            playsound("kicsongo.mp3")
    else:
        print("becsongo.mp3 és kicsongo.mp3 hiányzik, ezért nem lesz hangos értesítés...")

def task(oraszam):
    print("Ertesites es hang kuldese folyamatban...")
    # Páros
    if((oraszam % 2) == 0):
        cosz = int(((oraszam) / 2) + 1)
        notification.notify(
            title='🔔 ➡ ' + str(cosz) + '.',
            message='Becsengettek az órára',
            app_name='Csengoapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    # Páratlan
    elif((oraszam % 2) != 0):
        cosz = int(((oraszam) / 2) + 0.5)
        notification.notify(
            title=str(cosz) + '. ➡ 📕',
            message='Véget ért az óra',
            app_name='Csengoapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    else:
        schedule.clear('ertesites')
        sys.exit()


def main():
    x = datetime.datetime.now()
    print("A program elindult")
    print("Beütemezett értesítések:")
    if(calendar.weekday(x.year, x.month, x.day) >= 5):
        notification.notify(
            title='🔕 ➡ Ma nincsenek órák',
            message='Élvezd a hétvége nyugalmát :)',
            app_name='Csengoapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        runtime = False
    elif(strftime("%H:%M") >= adatbazis[-1]):
        notification.notify(
            title='🔕 ➡ Véget ért az összes óra',
            message='Élvezd a délután nyugalmát :)',
            app_name='Csengoapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        runtime = False
    else:
        runtime = True
        notification.notify(
            title='🛎️ ➡ Csengőapp mostantól aktív',
            message='Innentől értesítéseket fogsz kapni az órarendnek megfelelően!',
            app_name='Csengoapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )

    # Beütemezés
    for i, ido in enumerate(adatbazis):
        schedule.every().day.at(ido).do(task, oraszam=i).tag('ertesites')
        
    while runtime == True:
        schedule.run_pending()
        time.sleep(1)

    print("Minden beütemzett értesítésnek vége, a program leáll...")


if __name__ == "__main__":
    main()