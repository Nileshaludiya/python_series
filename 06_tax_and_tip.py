# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places

meal = input("Enter  meal cost: ")
tax = input("Enter tax rate: ")
tip = input("Enter tip rate: ")
tax_amount = (float(meal)*float(tax))/100
tip_amount = (float(meal)*float(tip))/100
total = float(meal) + tax_amount + tip_amount
print("Total Amount: ",total)