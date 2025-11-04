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

# Get date difference

from datetime import datetime

d1 = datetime(2025, 10, 16)
d2 = datetime(2025, 8, 1)

diff = d1 - d2
print("difference in days: ", diff.days)

# check if date is expired

expiry_date = datetime(2025, 10, 10)

today = datetime.now()
if today > expiry_date:
    print("Expired")
else:
    print("Active")

# get start and end of day

today = datetime.now()
start_of_day = datetime(today.year, today.month, today.day, 0, 0, 0)
end_of_day = datetime(today.year, today.month, today.day, 23, 59, 59)
print("start of day", start_of_day)
print("end of day", end_of_day)

# calculate age or duration between dates

dob = date(1995, 12, 30)
today = date.today()

age_years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
print("Age: ", age_years, "years")

# get the first day of current month

today = date.today()
first_day = today.replace(day=1)
print("first day of month", first_day)

# get first day of a particular month

year = 2025
month = 3
first_day_of_month = date(year, month, 1)
print("first day of march 2025", first_day_of_month)

# get weekday name

today = date.today()

week_name = today.strftime("%A")
short_week_name = today.strftime("%a")
month_name = today.strftime("%B")
short_month_name = today.strftime("%b")
year_name_4_digit = today.strftime("%Y")
year_name_2_digit = today.strftime("%y")
print(week_name)
print(short_week_name)
print(month_name)
print(short_month_name)
print(year_name_4_digit)
print(year_name_2_digit)