# The ideal gas law is a mathematical approximation of the behavior of gasses as
# pressure, volume and temperature change. It is usually stated as:
# PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, n is the amount of
# substance in moles, R is the ideal gas constant, equal to 8.314 mol K J , and T is the
# temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies
# the pressure, volume and temperature. Test your program by determining the number
# of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
# a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
# approximately 20 degrees Celsius or 68 degrees Fahrenheit.

P = int(input("Enter value of Pressure(in pascal): "))
V = int(input("Enter value of Volume(Liters me): "))
T = int(input("Enter temperature of value(Celsius me): "))
R = 8.314
T_kelvin = T + 273.15
n = (P*V)/(R*T)
print("Number of moles of gas:",n)