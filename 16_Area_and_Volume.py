# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = πr2. The
# volume of a sphere is computed using the formula volume = 43πr3.

r = float(input("Enter value of radius: "))
pi = 3.14
print("area of circle:",pi*r**2)
print("The volume of a with radius r:",4/3*(pi*(r**3)))