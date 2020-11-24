from datetime import *

# datetime.date
today = date.today()
date_formatted = today.strftime('%d-%m-%Y\n')
print(date_formatted)

# datetime.time
time = time(9, 23, 53, 244852)
print(time)
time_formatted = time.strftime('%H:%M:%S\n')
print(time_formatted)

# datetime.datetime
datetime = datetime.now()
print(datetime)
date_today = datetime.strftime('%d-%m-%Y')
time_now = datetime.strftime('%H:%M:%S\n')
print(date_today)
print(datetime.strftime('%d %B, %Y'))
print(time_now)

# datetime.timedelta
time1 = date(2005, 6, 7)
time2 = date.today()
time_dif = time2 - time1
print(time_dif, type(time_dif))
