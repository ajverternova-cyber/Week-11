# 1.Write a program that takes 2 numbers as input and outputs their sum, difference and product in separate lines.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)


# 2.Write a program that takes an integer as input and outputs whether the input is positive, negative or zero.

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 3.Write a program that takes a grade (0-100) as input and outputs “A” if it’s 80+, “B” if it’s 60-79, “C” if it’s 40-59 and “F” below 40. Implement handling for illegal input.

try:
    grade = int(input("Enter grade (0-100): "))

    if grade < 0 or grade > 100:
        print("Illegal input")
    elif grade >= 80:
        print("A")
    elif grade >= 60:
        print("B")
    elif grade >= 40:
        print("C")
    else:
        print("F")

except:
    print("Illegal input")


# 4.Write a program that repeatedly asks the user for input until 5 inputs are received. Output the sum of all those inputs without using lists.

count = 0
total = 0

while count < 5:
    num = float(input("Enter a number: "))
    total += num
    count += 1

print("Sum:", total)

# 5.Write a program that takes an input and will output a pyramid of asterix based on the number of layers given as input.

layers = int(input("Enter number of layers: "))

for i in range(1, layers + 1):
    print("*" * i)

# 6.Write a program that prints all numbers 1-20 but prints X if the number is divisible by 3.

for i in range(1, 21):
    if i % 3 == 0:
        print("X")
    else:
        print(i)


# 7.Write a program that declares a list with 5 elements, changes the 3rd element to 99 and outputs the changed list.

numbers = [1, 2, 3, 4, 5]
numbers[2] = 99

print(numbers)

# 8.Write a program that declares a list and outputs the reverse of that list without using built-in functions that handle lists.

numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)

# 9.Write a program that declares a tuple with 3 elements and changes the middle element to 99 before outputting the changed tuple.

my_tuple = (1, 2, 3)

temp_list = list(my_tuple)
temp_list[1] = 99
my_tuple = tuple(temp_list)

print(my_tuple)

# 10.Write a function that takes 2 numbers as arguments and returns the sum and product. Call the function and output the results.


def calculate(a, b):
    return a + b, a * b


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result, product_result = calculate(num1, num2)

print("Sum:", sum_result)
print("Product:", product_result)

# 11.Write a function that takes a number and returns whether the number is Odd or Even. Call the function with user input.


def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


number = int(input("Enter a number: "))
print(check_even_odd(number))

# 12.Write a program that declares a list and outputs the sum of all elements inside the list without using built in functions that handle lists.

numbers = [1, 2, 3, 4, 5]

total = 0
for num in numbers:
    total += num

print("Sum:", total)

# 13.Write a program that takes 5 inputs from a user and stores them in a list. Write 3 functions that respectively returns the smallest number, largest number and sum of elements.

numbers = []

for i in range(5):
    num = float(input("Enter number: "))
    numbers.append(num)


def smallest(lst):
    min_value = lst[0]
    for num in lst:
        if num < min_value:
            min_value = num
    return min_value


def largest(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


def total_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total


print("Smallest:", smallest(numbers))
print("Largest:", largest(numbers))
print("Sum:", total_sum(numbers))
