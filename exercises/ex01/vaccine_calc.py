"""A vaccination calculator."""

__author__ = "730342553"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


total_pop: int = int(input("Population: "))
doses: int = int(input("Doses administered: "))
dpd: int = int(input("Doses per day: "))
target_int: int = int(input("Target percent vaccinated: "))

target: int = (target_int / 100)
now_pop: int = (total_pop - (doses / 2))
goal_days: int = (((now_pop * 2) * target) / dpd)



final: datetime = datetime.today() + timedelta(goal_days)




print("We will reach " + target_int + " % vaccination in " + goal_days + ", which falls on " + final.strftime("%B %d, %Y") + ".")




