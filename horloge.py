import time
from time import strftime

def horloge():
    heure = int(strftime('%H'))
    minute = int(strftime('%M'))
    seconde = int(strftime('%S'))
    
    while True:
        if seconde == 60:
            seconde = 0
            minute += 1
            if minute == 60:
                minute = 0
                heure += 1
        affichage=(str(heure).rjust(2,'0')+":"+str(minute).rjust(2,'0')+":"+str(seconde).rjust(2,'0'))
        seconde += 1
        print(affichage)
        time.sleep(1)
        
horloge()