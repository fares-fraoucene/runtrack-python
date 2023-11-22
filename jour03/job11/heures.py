def time(minute):
    heure = minute // 60
    minute = minute % 60
    print(f'{heure} h et {minute} min')


time(1)
time(60)
time(240)