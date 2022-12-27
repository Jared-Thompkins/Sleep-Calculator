from datetime import timedelta, datetime, date


today = date.today()
tomorrow = today + timedelta(days=1)

tomorrow_with_time = datetime(
    year=tomorrow.year,
    month=tomorrow.month,
    day=tomorrow.day,
)

import datetime
wake_time_after_midnight = timedelta(hours=6) + timedelta(minutes=00)
tomorrow_wake_time = tomorrow_with_time + wake_time_after_midnight
current_time = datetime.datetime.now()

time_till_wakeup = tomorrow_wake_time - current_time

print("Bedtimes")
six_cycle_sleep_time = (wake_time_after_midnight + tomorrow_with_time) - timedelta(hours=9)
five_cycle_sleep_time = (wake_time_after_midnight + tomorrow_with_time) - timedelta(hours=7.5)
four_cycle_sleep_time = (wake_time_after_midnight + tomorrow_with_time) - timedelta(hours=6)
print("Six Cycle:", six_cycle_sleep_time.time())
print("Five Cycle:", five_cycle_sleep_time.time())
print("Four Cycle:", four_cycle_sleep_time.time())


time_left_before_six_cycle = six_cycle_sleep_time - current_time
time_left_before_five_cycle = five_cycle_sleep_time - current_time
time_left_before_four_cycle = four_cycle_sleep_time - current_time

print(" ")

print("Time left to make Bedtimes")
print("For 6 cycles, fall asleep in:", time_left_before_six_cycle)
print("For 5 cycles, fall asleep in:", time_left_before_five_cycle)
print("For 4 cycles, fall asleep in:", time_left_before_four_cycle)


def function(wake_time):
    return wake_time - timedelta(hours=9)

print(function(timedelta(hours=6)))

