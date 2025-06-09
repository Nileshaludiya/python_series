# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that
# they occupy exactly two digits, with a leading 0 displayed if necessary.

T_S = int(input("Enter total second: "))
D = T_S//86400
S = T_S%86400

H = S//3600
S = S%3600

M = S//60
S = S%60

print(f"{D}:{H:02}:{M:02}:{S:02}")
