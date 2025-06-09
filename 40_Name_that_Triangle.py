# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

side1 = int(input("Enter value of first side: "))
side2 = int(input("Enter value of second side: "))
side3 = int(input("Enter value of third side: "))
if side1 == side2 == side3:
    print("This triangle is equilateral triangle")
elif side3 != side1 != side2:
    print("This triangle is scalene triangle")
else:
    print("This triangle is isosceles triangle")
