# In this exercise you will create a program that reads a pressure from the user in 
# kilopascals. Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units

pressure = int(input("Enter pressure(in kilopascals): "))
print(f"pressure in pounds per square inch: {pressure* 0.145038} psi")
print(f"pressure in millimeters of mercury: {pressure*7.50062} mmHg")
print(f"pressure in Atmospheres: {pressure* 0.00986923} atm")