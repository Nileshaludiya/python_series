# Python includes a library of functions for working with time, including a function
# called asctime in the time module. It reads the current time from the computer’s internal clock and returns it in a human-readable format. Write a program
# that displays the current time and date. Your program will not require any input from
# the user.

from datetime import datetime
now = datetime.now()
print(now)