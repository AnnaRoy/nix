import datetime

today = datetime.datetime.now()

d = datetime.datetime(today.year, today.month, today.day, 23, 22, 31)


def minutes_to_midnight(d):
    today = datetime.datetime.now()
    time = datetime.datetime(today.year, today.month, today.day, 0, 0, 0) - d
    minuts = round(time.seconds / 60)
    return f'{minuts} minutes'


##################################################

def minutes_to_midnight2(d):
    res = round(24 * 60 - d.hour * 60 - d.minute - d.second / 60)
    return f"{res} minute{'s' if res > 1 else ''}"


minutes_to_midnight(d)
minutes_to_midnight2(d)