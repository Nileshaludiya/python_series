# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

length = input("Enter length of room: ")
width = input("Enter width of room: ")
print("area of the field in acres: ",(int(length)*int(width))/43560)