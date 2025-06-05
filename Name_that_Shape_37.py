# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

side = int(input("Enter a value from 3 to 10: "))
if side == 3:
    print("This is Triangle")
elif side == 4:
    print("This is Quadrangle")
elif side == 5:
    print("This is Pentagon")
elif side == 6:
    print("This is Hexagon")
elif side == 7:
    print("This is Heptagon")
elif side == 8:
    print("This is Octagon")
elif side == 9:
    print("This is Nonagon")
elif side == 10:
    print("This is Decagon")
else:
    print("error: please enter a number between 3 and 10")
    