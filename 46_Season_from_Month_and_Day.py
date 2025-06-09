# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:
# Season First day
# Spring March 20
# Summer June 21
# Fall September 22
# Winter December 21
# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

day = int(input("Enter day of today: "))
month = input("Enter present month: ").lower()
if month == 'january':
    month_num = 1
elif month == 'february':
    month_num = 2
elif month == 'march':
    month_num = 3
elif month == 'april':
    month_num = 4
elif month == 'may':
    month_num = 5
elif month == 'june':
    month_num = 6
elif month == 'july':
    month_num = 7
elif month == 'august':
    month_num = 8
elif month == 'september':
    month_num = 9
elif month == 'october ':
    month_num = 10
elif month == 'november':
    month_num = 11
elif month == 'december':
    month_num = 12

if ((month_num == 3 and day >= 20) or (month_num > 3 and month_num < 6) or (month_num == 6 and day <= 20)):
    print("Spring")
elif ((month_num == 6 and day >= 21) or (month_num > 6 and month_num < 9) or (month_num == 9 and day <= 21)):
    print("Summer")
elif ((month_num == 9 and day >= 22) or (month_num > 9 and month_num < 12) or (month_num == 12 and day <= 22)):
    print("Fall")
else:
    print("Winter")