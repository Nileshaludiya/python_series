# At a particular university, letter grades are mapped to grade points in the following
# manner:
# Letter Grade points
# A+ 4.0
# A 4.0
# A− 3.7
# B+ 3.3
# B 3.0
# B− 2.7
# C+ 2.3
# C 2.0
# C− 1.7
# D+ 1.3
# D 1.0
# F 0
# Write a program that begins by reading a letter grade from the user. Then your
# program should compute and display the equivalent number of grade points. Ensure
# that your program generates an appropriate error message if the user enters an invalid
# letter grade

grade = input("Enter your grade: ").upper()
if grade == 'A+' or grade == 'A':
    print("Number of grade: 4.0")
elif grade == 'A-':
    print("Number of grade: 3.7")
elif grade == 'B+':
    print("Number of grade: 3.3")
elif grade == 'B':
    print("Number of grade: 3.0")
elif grade == 'B-':
    print("Number of grade: 2.7")
elif grade == 'C+':
    print("Number of grade: 2.3")
elif grade == 'C':
    print("Number of grade: 2.0")
elif grade == 'C-':
    print("Number of grade: 1.7")
elif grade == 'D+':
    print("Number of grade: 1.3")
elif grade == 'D':
    print("Number of grade: 1.0")
elif grade == 'F':
    print("Number of grade: 0")
else:
    print("Invalid grade entered. Please enter a valid letter grade ")