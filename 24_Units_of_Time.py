# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

D = int(input("Enter value of day: "))
H = int(input("Enter value of hours(0 to 23): "))
M = int(input("Enter value of minutes(0 to 59): "))
S = int(input("Enter value of seconds(0 to 59): "))
# H = H + D * 24
# M = M + H * 60
Total_S = D*86400 + H*3600 + M*60 + S
print("total number of seconds:",Total_S)