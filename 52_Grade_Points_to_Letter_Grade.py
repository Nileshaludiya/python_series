# In the previous exercise you created a program that converts a letter grade into the
# equivalent number of grade points. In this exercise you will create a program that
# reverses the process and converts from a grade point value entered by the user to a
# letter grade. Ensure that your program handles grade point values that fall between
# letter grades. These should be rounded to the closest letter grade. Your program
# should report A+ for a 4.0 (or greater) grade point average

grade = float(input("Enter grade point average: "))
if 0 <= grade < 1.0:
    print("F grade")
elif 1.0 <= grade < 1.3:
    print("D grade")
elif 1.3 <= grade < 1.7:
    print("D+ grade")
elif 1.7 <= grade < 2.0:
    print("C- grade")
elif 2.0 <= grade < 2.3:
    print("C grade")
elif 2.3 <= grade < 2.7:
    print("C+ grade")
elif 2.7 <= grade < 3.0:
    print("B- grade")
elif 3.0 <= grade < 3.3:
    print("B grade")
elif 3.3 <= grade < 3.7:
    print("B+ grade")
elif 3.7 <= grade < 4.0:
    print("A- grade")
elif grade == 4.0:
    print("A grade")
elif grade > 4.0:
    print("A+ grade")
else:
    print("Invalid grade")