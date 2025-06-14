# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))

# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.

# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.

# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians.

import math
EARTH_RADIUS_KM = 6371.01

t1 = float(input("Enter the latitude of point 1 (in degree): "))
g1 = float(input("Enter the longitude of point 1 (in degree): "))
t2 = float(input("Enter the latitude of point 2 (in degree): "))
g2 = float(input("Enter the langitude of point 2 (in degree): "))

t1_rad = math.radians(t1) 
g1_rad = math.radians(g1) 
t2_rad = math.radians(t2) 
g2_rad = math.radians(g2) 

print(t1_rad)
# print(g1)
# print(t2)
# print(math.acos(
#     math.sin(t1_rad)
# ))

distance = EARTH_RADIUS_KM*math.acos(
    math.sin(t1_rad)*math.sin(t2_rad)+math.cos(t1_rad)*math.cos(t2_rad)*math.cos(g1_rad - g2_rad)
)

print(f"The distance betbeen the two points is {distance:.2} kilometers")