# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

feet = int(input("Enter Feet value: "))
print("The value in Inche:",feet*12)
print("The value in Yard:",feet/3)
print("The value in Miles:",feet/8280)