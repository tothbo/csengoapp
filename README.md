# CsengőAPP

Egy Python alapú értesítő alkalmazás Windows-ra.

# Leírás

A kötelező otthon maradás keretében úgy éreztük kellene valami ami mindig értesít az Online óráinkról 

# Telepítés

Szükséges csomagok a requirements.txt-ben mellékelve.

1. Hozz létre egy mappát olyan névvel, amit meg tudsz jegyezni (jelen esetben: csengo_app)

2. Nyiss egy parancssort (kereső -> cmd.exe), és csekkold le, hogy telepítve van-e a pip (pip --version)

3. Telepítsd a szükséges csomagokat pippel:

 `pip install -r D:\csengo_app\requirements.txt`
 (vagy ahol a mappa van, a requirements.txt mellékelve)

4. Indítsd el a csengoapp.py-t, és már menni is fog :)

Ezek mellett érdemes a bgcsengoapp.pyw fájl hozzáadni induláshoz.

Minden jog fenntartva, még az is ami nem létezik.
#csengoapp, #csengoappsquad

# Timetable.txt formátuma

A timetable.txt ben tudod megadni a (még mai) órákat.
A fájlban egy órát két sor határot meg:

1. Az első sor egy óranévből és, egy szóközzel elválasztva, egy becsöngetése időpontból áll.
2. A második sor egy kicsöngetése időpontból áll.

Pl.:

Matek 13:00
13:40

Az időpont formátuma : ÓÓ:PP (Ó = Óra, P=Perc)


