import datetime


def get_bedtime(tomorrow_wake_time: str) -> str:
    tomorrow_wake_time_dt = datetime.datetime.strptime(tomorrow_wake_time, '%I:%M %p')
    bedtime_dt = tomorrow_wake_time_dt - datetime.timedelta(hours=9)
    sleep_time = bedtime_dt.strftime('%I:%M %p')

    return sleep_time


bedtime = get_bedtime('10:30 AM')
print(bedtime)
