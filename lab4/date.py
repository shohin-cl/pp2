from datetime import timedelta, datetime
import time

"""
Python date
1)Write a Python program to subtract five days from current date.
2)Write a Python program to print yesterday, today, tomorrow.
3)Write a Python program to drop microseconds from datetime.
4)Write a Python program to calculate two date difference in seconds.
"""
#Task 1
today = datetime.now()
print(today - timedelta(days = 5))

#Task 2
yesterday = (today - timedelta(days = 1))
tomorrow = (today + timedelta(days = 1))

print(f"Yesterday: {yesterday}, Today: {today}, Tomorrow: {tomorrow}")

#Task 3
date_without_microsec = today.replace(microsecond=0)
print(date_without_microsec)

#Task 4

n = int(input())
date1 = today
date2 = today + timedelta(days = n)

print(f"Difference between {n} days:", (date2-date1).total_seconds())
