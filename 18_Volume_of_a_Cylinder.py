# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the volume, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.
pi = 3.14
radius = int(input("Enter a value of radius of cylinder: "))
height = int(input("Enter the height of the cylinder: "))
volume = pi * radius**2 * height
print("circular volume = ",round(volume,1))
print(f"circular volume = {volume:.1f}")