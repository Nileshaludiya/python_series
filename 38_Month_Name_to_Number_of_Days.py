# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.

month = input("Enter month name(in small letter): ")
if month == 'january':
    print("There are 31 days in january")
elif month == 'february':
    print("There are 28 and 29 days in february")
elif month == 'march':
    print("There are 31 days in march")
elif month == 'april':
    print("There are 30 days in april")
elif month == 'may':
    print("There are 31 days in may")
elif month == 'june':
    print("There are 30 days in june")
elif month == 'july':
    print("There are 31 days in july")
elif month == 'august':
    print("There are 31 days in august")
elif month == 'september':
    print("There are 30 days in september")
elif month == 'october':
    print("There are 31 days in october")
elif month == 'november':
    print("There are 30 days in november")
elif month == 'december':
    print("There are 31 days in december")
else:
    print("Invalid Month Name")