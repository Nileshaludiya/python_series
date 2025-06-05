# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

feet = int(input("Enter height in Feet: ")) 
inche = int(input("Enter height in Inche: "))
total_inche = inche + (feet*12) 
centimeters = 2.54*total_inche
print("height in centimeter: ",centimeters)