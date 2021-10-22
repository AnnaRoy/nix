from datetime import datetime

times = ["01:00:00", "02:30:00", "22:00:00"]
day = 86400

def determine_time(times):
    times_sec = []
    for i in times:
        result = datetime.time(datetime.strptime(i, "%H:%M:%S"))
        b = result.hour * 3600 + result.minute * 60 + result.second * 60
        times_sec.append(b)
    print(sum(times_sec)<= day)
    print(type(result))
    return sum(times_sec)<= day

determine_time(times)

####################################################################################

def determine_time2(times):
    time = 0
    for duration in times:
        hours, minutes, seconds = map(int, duration.split(":"))#разбивает строку (str) по разделителю записывая в з-и переменные
        time += 3600*hours + 60*minutes + seconds
    print(time <= 86400)
    return time <= 86400

determine_time2(times)