# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.

import math
a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
print("The sum of A & B:",a+b)
print("when B is subtracted from A:",a-b)
print("The product of A & B:",a*b)
print("The quotient when A is divided by B:",a/b)
print("The remainder when A is divided by B:",a%b)
print("The result of log10 A:",math.log10(a))
print("The result of A^B",math.pow(a,b))