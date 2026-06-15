""" To write a function which given two dates, checks whether the dates are
exactly 1 month apart (e.g June 06 2011 & July 06 2011, Dec 15 2010 &
Jan 15 2011), less than 1 month apart (e.g Mar 01 2011 & Mar 25 2011)
"""

from datetime import datetime
def check_date_gap():
    date_str1 = input("Enter first date (e.g., June 06 2011): ")
    date_str2 = input("Enter second date (e.g., July 06 2011): ")
    d1 = datetime.strptime(date_str1, "%B %d %Y")
    d2 = datetime.strptime(date_str2, "%B %d %Y")
    d1, d2 = min(d1, d2), max(d1, d2)
    next_month = 1 if d1.month == 12 else d1.month + 1
    next_year = d1.year + 1 if d1.month == 12 else d1.year
    target_date = datetime(next_year, next_month, d1.day)
    if d2 == target_date:
        print("Exactly 1 month apart")
    elif d2 < target_date:
        print("Less than 1 month apart")
    else:
        print("More than 1 month apart")
check_date_gap()
