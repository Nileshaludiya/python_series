# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.

# Toonie = 200 cents

# Loonie = 100 cents

# Quarter = 25 cents

# Dime = 10 cents

# Nickel = 5 cents

# Penny = 1 cent


value = int(input("Enter the Amount in cents: "))
Toonie = value//200
print("Toonie",Toonie)
value %= 200
Loonie = value//100
print("Loonie",Loonie)
value %= 100
Quarter = value//25
print("Quarter",Quarter)
value %= 25
Dime = value//10
print("Dime",Dime)
value %= 10
Nickel = value//5
print("Nickel",Nickel)
value %= 5
Penny = value//1
print("Penny",Penny)
value %= 1
