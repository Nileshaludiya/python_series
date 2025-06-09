# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:
# Zodiac sign Date range
# Capricorn December 22 to January 19
# Aquarius January 20 to February 18
# Pisces February 19 to March 20
# Aries March 21 to April 19
# Taurus April 20 to May 20
# Gemini May 21 to June 20
# Cancer June 21 to July 22
# Leo July 23 to August 22
# Virgo August 23 to September 22
# Libra September 23 to October 22
# Scorpio October 23 to November 21
# Sagittarius November 22 to December 21
# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message.

day = int(input("Enter day of your birth: "))
month = input("Enter month of your birth: ").lower()
if month == 'january':
    month_num = 1
elif month == 'february':
    month_num = 2
elif month == 'march':
    month_num = 3
elif month == 'april':
    month_num = 4
elif month == 'may':
    month_num = 5
elif month == 'june':
    month_num = 6
elif month == 'july':
    month_num = 7
elif month == 'august':
    month_num = 8
elif month == 'september':
    month_num = 9
elif month == 'october ':
    month_num = 10
elif month == 'november':
    month_num = 11
elif month == 'december':
    month_num = 12

if ((month_num == 1 and day >= 20) or (month_num == 2 and day <= 18)):
    print("Aquarius")
if ((month_num == 2 and day >= 19) or (month_num == 3 and day <= 20)):
    print("Pisces")
if ((month_num == 3 and day >= 21) or (month_num == 4 and day <= 19)):
    print("Aries")
if ((month_num == 4 and day >= 20) or (month_num == 5 and day <= 20)):
    print("Taurus")
if ((month_num == 5 and day >= 21) or (month_num == 6 and day <= 20)):
    print("Gemini")
if ((month_num == 6 and day >= 21) or (month_num == 7 and day <= 22)):
    print("Cancer")
if ((month_num == 7 and day >= 23) or (month_num == 8 and day <= 22)):
    print("Leo")
if ((month_num == 8 and day >= 23) or (month_num == 9 and day <= 22)):
    print("Virgo")
if ((month_num == 9 and day >= 23) or (month_num == 10 and day <= 22)):
    print("Libra")
if ((month_num == 10 and day >= 23) or (month_num == 11 and day <= 21)):
    print("Scorpio")
if ((month_num == 11 and day >= 22) or (month_num == 12 and day <= 21)):
    print("Sagittarius")
if ((month_num == 12 and day >= 22) or (month_num == 1 and day <= 19)):
    print("Capricorn")