# On what day of the week were you born? If you don't know the answer to this, use the calendar library to get the answer.

import calendar 

year = int(input("enter your birth year (e.g., 2000):"))
month = int(input("enter your birth year (e.g., 1-12):"))
day = int(input("enter your birth year (e.g., 1-31):"))

weekday_numbers = calendar.weekday(year,month,day)
days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
print("you were born on a", days[weekday_numbers])