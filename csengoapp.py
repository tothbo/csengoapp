from plyer import notification
import time
import datetime
from time import strftime
import schedule
from playsound import playsound
import calendar
import os.path

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
        print("becsongo.mp3 or kicsongo.mp3 is missing...")

def task(oraszam):
    print("Ertesites es hang kuldese folyamatban...")
    if(oraszam == 0):
        notification.notify(
            title='🔔 ➡ 1.',
            message='Becsengettek az első órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 1):
        notification.notify(
            title='1. ➡ 📕',
            message='Véget ért az első óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 2):
        notification.notify(
            title='🔔 ➡ 2.',
            message='Becsengettek a második órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 3):
        notification.notify(
            title='2. ➡ 📕',
            message='Véget ért a második óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 4):
        notification.notify(
            title='🔔 ➡ 3.',
            message='Becsengettek a harmadik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 5):
        notification.notify(
            title='3. ➡ 📕',
            message='Véget ért a harmadik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 6):
        notification.notify(
            title='🔔 ➡ 4.',
            message='Becsengettek a negyedik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 7):
        notification.notify(
            title='4. ➡ 📕',
            message='Véget ért a negyedik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 8):
        notification.notify(
            title='🔔 ➡ 5.',
            message='Becsengettek az ötödik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 9):
        notification.notify(
            title='5. ➡ 📕',
            message='Véget ért az ötödik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 10):
        notification.notify(
            title='🔔 ➡ 6.',
            message='Becsengettek a hatodik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 11):
        notification.notify(
            title='6. ➡ 📕',
            message='Véget ért a hatodik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 12):
        notification.notify(
            title='🔔 ➡ 7.',
            message='Becsengettek a hetedik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 13):
        notification.notify(
            title='7. ➡ 📕',
            message='Véget ért a hetedik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
    elif(oraszam == 14):
        notification.notify(
            title='🔔 ➡ 8.',
            message='Becsengettek a nyolcadik órára',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(1)
        print("Siker!")
    elif(oraszam == 15):
        notification.notify(
            title='8. ➡ 📕',
            message='Véget ért a nyolcadik óra',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        csongo(2)
        print("Siker!")
        exit()
    else:
        schedule.clear('ertesites')


def main():
    x = datetime.datetime.now()
    print("Started")
    print("List of scheduled jobs:")
    if(calendar.weekday(x.year, x.month, x.day) >= 5):
        notification.notify(
            title='🔕 ➡ Ma nincsenek órák',
            message='Élvezd a hétvége nyugalmát :)',
            app_name='Csengőapp',
            app_icon='icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
            toast=False,
        )
        runtime = False
    elif(strftime("%H:%M") >= adatbazis[-1]):
        notification.notify(
            title='🔕 ➡ Véget ért az összes óra',
            message='Élvezd a délután nyugalmát :)',
            app_name='Csengőapp',
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
            app_name='Csengőapp',
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

    print("Everything done! Shutting down...")


if __name__ == "__main__":
    main()
