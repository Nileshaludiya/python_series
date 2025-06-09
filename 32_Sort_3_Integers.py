# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))
num3 = int(input("Enter third value: "))
min_value = min(num1,num2,num3)
max_value = max(num1,num2,num3)
middel_value = (num1+num2+num3)-(min_value+max_value)
print(f"The numbers in sorted order are: {min_value} {middel_value} {max_value}")