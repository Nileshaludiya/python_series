# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:
# Magnitude Descriptor
# Less than 2.0 Micro
# 2.0 to less than 3.0 Very minor
# 3.0 to less than 4.0 Minor
# 4.0 to less than 5.0 Light
# 5.0 to less than 6.0 Moderate
# 6.0 to less than 7.0 Strong
# 7.0 to less than 8.0 Major
# 8.0 to less than 10.0 Great
# 10.0 or more Meteoric
# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake

magnitude = float(input("Enter the earthquake magnitude: "))
if magnitude < 2.0:
    print("Micro")
elif 2.0 <= magnitude < 3.0:
    print("Very Minor")
elif 3.0 <= magnitude < 4.0:
    print("Minor")
elif 4.0 <= magnitude < 5.0:
    print("Light")
elif 5.0 <= magnitude < 6.0:
    print("Moderate")
elif 6.0 <= magnitude < 7.0:
    print("Strong")
elif 7.0 <= magnitude < 8.0:
    print("Major")
elif 8.0 <= magnitude < 10.0:
    print("Great")
elif magnitude >= 10.0:
    print("Meteoric")