# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet.

Celsius_temperature = int(input("Enter value of temperature(in degrees Celsius): "))
Fahrenheit_temperature = (Celsius_temperature*(9/5))+32
print("temperature:",Fahrenheit_temperature,"F")
print("temperature:",Celsius_temperature+273.15,"K")
