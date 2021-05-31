# Program to display calendar of the given month and year

# importing calendar module
import calendar
import datetime

yy = 2021  # year
mm = 1  # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

# using calender to print calendar of year
# prints calendar of 2021
print("The calender of year 2021 is : ")
print(calendar.calendar(2021, 2, 1, 6))

datetime_object = datetime.datetime.now()
print("Current Date and Time: %s" %  datetime_object)

date_object = datetime.date.today()
print("Today: %s" % date_object)