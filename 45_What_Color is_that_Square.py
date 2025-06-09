# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below
# Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking

# co = input("Enter chess board position: ").lower()
# if co == 'a1' or co == 'a3'or co == 'a5' or co == 'a7' or co == 'b2' or co == 'b4'or co == 'b6' or co == 'b8' or co == 'a1' or co == 'c1'or co == 'c3' or co == 'c5' or co == 'c7' or co == 'd2' or co == 'd4' or co == 'd6' or co == 'd8' or co == 'e1' or co == 'e3' or co == 'e5' or co == 'e7' or co == 'f2' or co == 'f4' or co == 'f6' or co == 'f8' or co == 'g1' or co == 'g3' or co == 'g5' or co == 'g7' or co == 'h2' or co == 'h4' or co == 'h6' or co == 'h8':
#     print('black')
# else:
#     print ("white")

row = input("Enter row value(a to h): ").upper()
colomn = int(input("Enter colomn value(1 to 8): "))
num_row = ord(row)
if (colomn + num_row) % 2 == 0:
    print("black")
else:
    print("white")