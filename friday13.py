import datetime

def friday_13th(year, month):
    day = datetime.datetime(year, month, 13)
    day2 = day.weekday()
    if day2 == 4:
        return True
    return False

print(friday_13th(2043,4))


