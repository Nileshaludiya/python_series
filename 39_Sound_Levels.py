# Jackhammer 130
# Gas lawnmower 106
# Alarm clock 70
# Quiet room 40
# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.

noise = int(input("Enter a decibel value: "))
if noise < 40:
    print("This noise is Quiet room")
elif 40 < noise < 70:
    print("This noise is Alarm clock")
elif 70 < noise < 106:
    print("This noise is Gas lawnmower")
else:
    print("This noise is Jackhammer")
    