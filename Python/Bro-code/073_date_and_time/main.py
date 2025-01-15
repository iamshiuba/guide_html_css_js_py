import datetime

date = datetime.date(2025,1,2)
print(date)
today = datetime.date.today()
print(today)

time = datetime.time(12,30,0)
print(time)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %m-%d-%Y")
print(now)

target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("target date has passed")
else:
    print("target date has NOT passed")