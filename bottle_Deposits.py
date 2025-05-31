# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

small_container = input("Enter the value of 1 liter or smaller container: ")
big_container = input("Enter the value for a container larger than 1 liter: ")
total = (float(small_container)*0.10) + (float(big_container)*0.25)
print("your total refund will be $",total)