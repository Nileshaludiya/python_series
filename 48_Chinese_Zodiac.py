# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table below. The pattern repeats from there, with 2012 being another
# year of the dragon, and 1999 being another year of the hare.
# Year Animal
# 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare
# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table.

year = int(input("Enter year: "))
index = (year - 2000)%12
if index == 0:
    print("Dragon")
elif index == 1:
    print("Snake")
elif index == 2:
    print("Horse")
elif index == 3:
    print("Sheep")
elif index == 4:
    print("Monkey")
elif index == 5:
    print("Rooster")
elif index == 6:
    print("Dog")
elif index == 7:
    print("Pig")
elif index == 8:
    print("Rat")
elif index == 9:
    print("Ox")
elif index == 10:
    print("Tiger")
elif index == 11:
    print("Hare")