from datetime import datetime, timedelta, date


# get current date and time
now = datetime.now()
print("current date time ", now)
print("current date ", now.date())
print("current time ", now.time())

# compare with current date/time
today = datetime.now()
given_date = datetime(2025, 10, 15)
print("given_date ", given_date)

if given_date < today:
    print("Given date is in the past")
elif given_date > today:
    print("Given date is in the future")
else:
    print("Given date is today")

# Add or substract days, months, years
# python datetime  doesn't directly support months/years because months have variable lengths.
# but we can handle multiple ways

# Add or substract using timedelta
today = datetime.now()
future_date = today + timedelta(days=10)
past_date = today - timedelta(days=10)
print("future date", future_date)
print("past date", past_date)

# Add or substract hours, minutes, seconds
new_time = datetime.now() + timedelta(hours=5, minutes=30)
print(f"after 5 hr 30 min from now {today} {new_time}")

# add/substract months or years using dateutil.relativedelta

# from dateutil.relativedelta import relativedelta
#
# today = datetime.now()
# next_month = today + relativedelta(months=1)
# next_year = today + relativedelta(years=1)
# previous_month = today - relativedelta(months=1)
#
# print("next_month", next_month)
# print("next_year", next_year)
# print("previous_month", previous_month)

# Add a specific time to a date
from datetime import time

date_part = datetime(2025, 10, 6)
time_part = time(15, 30, 0)

combined = datetime.combine(date_part, time_part)
print("combined", combined)

# formatting date and time string

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)

# converting string into datetime

date_str = "2025-10-16 17:50:35"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(parsed)