# Perimeter and area of a rectangle with sides as 4 and 8
# Rectangle dimensions
length = 8
width = 4

# Calculations
perimeter = 2 * (length + width)
area = length * width

# Output
print("Perimeter of the rectangle:", perimeter)
print("Area of the rectangle:", area)

# Converting celsius temperature to fahrenheit and fahrenheit to celsius
# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# Fahrenheit to Celsius
fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = (fahrenheit_input - 32) * 5 / 9
print("Temperature in Celsius:", celsius_output)

# Script that will take a 2 digit number and will display the tens and ones digit
# Set a two-digit number
number = 47

tens = number // 10
ones = number % 10

print("Tens digit:", tens)
print("Ones digit:", ones)
