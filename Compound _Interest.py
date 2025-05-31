# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

amount = int(input("Enter your Amount: "))
one_year = round(((amount*4)/100)+amount ,2)
print("One year After Amount is ",one_year)
two_year = round(((one_year*4)/100)+one_year,2)
print("Two year After Amount is: ",two_year)
three_year = round(((two_year*4)/100)+two_year,2)
print("Three year After Amount is: ",three_year)