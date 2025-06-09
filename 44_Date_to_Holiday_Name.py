# Canada has three national holidays which fall on the same dates each year.
# Holiday Date
# New year’s day January 1
# Canada day July 1
# Christmas day December 25
# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.
# Canada has two additional national holidays, Good Friday and Labour Day,
# whose dates vary from year to year. There are also numerous provincial and
# territorial holidays, some of which have fixed dates, and some of which have
# variable dates. We will not consider any of these additional holidays in this
# exercise.


day = int(input("Enter day of today: "))
month = input("Enter present month: ").lower()
if day == 1 and month == 'january':
    print("Holiday of New year's day")
elif day == 1 and month == 'july':    
    print("Holiday of Canada day")
elif day == 5 and month == 'december':    
    print("Holiday of Christmas day")
else:
    print("Not a fixed date national holiday")