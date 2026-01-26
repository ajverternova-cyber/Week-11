# SEMINAR 10
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



# SEMINAR 11------------------------------------------------------------------------------------------------------------

#Program that asks for a student's name and score and assigns him a grade from A to F.
# Input student details
name = input("Enter student name: ")
score = float(input("Enter test score (0 - 100): "))

# Determine pass or fail
if score >= 50:
    result = "Pass"
else:
    result = "Fail"

# Assign grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

# Output
print("\nStudent Name:", name)
print("Score:", score)
print("Result:", result)
print("Grade:", grade)


# SEMINAR 12----------------------------------------------------------------------------------------------------------------

# 1. Odd and even counter
even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("\nTotal even numbers:", even_count)
print("Total odd numbers:", odd_count)

# 2. Pyramid layers from number of blocks

blocks = int(input("Enter number of blocks: "))

layers = 0
used_blocks = 0

while used_blocks + (layers + 1) <= blocks:
    layers += 1
    used_blocks += layers

print("Number of layers:", layers)

# 3. Student grading (loop, lists, sorting)

names = []
grades = []

while True:
    name = input("Enter student name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    score = float(input("Enter test score: "))

    # Determine grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    elif score >= 50:
        grade = "E"
    else:
        grade = "F"

    names.append(name)
    grades.append(grade)

# Display all student names
print("\nAll Students:")
print(names)

# Display all grades
print("\nAll Grades:")
print(grades)

# Display students with their grades
print("\nStudents and Grades:")
for i in range(len(names)):
    print(names[i], "-", grades[i])

# Optional: Sorting grades
print("\nGrades sorted ascending:")
print(sorted(grades))

print("Grades sorted descending:")
print(sorted(grades, reverse=True))


# 4. Consonants only uppercase
word = input("Enter a word: ")

word = word.upper()
vowels = "AEIOU"
result = ""

for letter in word:
    if letter not in vowels:
        result += letter

print("Result:", result)




# SEMINAR 13--------------------------------------------------------------------------------------------------------------------

# 1. Sort students by grade (descending) and print
names = ["beni", "andi", "linda", "diana"]
grades = [85, 92, 78, 90]

# Combine lists and sort by grade (descending)
students = list(zip(names, grades))
students.sort(key=lambda x: x[1], reverse=True)

print("Students sorted by grade (descending):")
for student in students:
    print(student[0], "-", student[1])


# 2. Find the largest element using loops
names = ["beni", "andi", "linda", "diana"]
grades = [85, 92, 78, 90]

max_grade = grades[0]
max_index = 0

for i in range(len(grades)):
    if grades[i] > max_grade:
        max_grade = grades[i]
        max_index = i

print("Congratulations", names[max_index] + "!")
print("You have the highest grade:", max_grade)


# 3. Check if a number is in a list and print its index
numbers = [10, 25, 7, 40, 18, 7]
search = int(input("Enter a number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Number found at index:", i)
        found = True
        break

if not found:
    print("Number not in list")



# 4. Remove duplicate values from a list (using loops)
numbers = [1, 3, 5, 3, 7, 1, 9, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List without duplicates:")
print(unique_numbers)



# 5. Lottery system (6 numbers from 1–49)
import random

# Generate lottery numbers
lottery_numbers = random.sample(range(1, 50), 6)

# User input
user_numbers = []
print("Enter 6 numbers between 1 and 49:")

while len(user_numbers) < 6:
    num = int(input("Enter number: "))
    if 1 <= num <= 49 and num not in user_numbers:
        user_numbers.append(num)
    else:
        print("Invalid or duplicate number, try again.")

# Now I check matches
correct = 0
for num in user_numbers:
    if num in lottery_numbers:
        correct += 1

# Now I calculate points
points = 0
if correct > 0:
    points = 2 ** (correct - 1)

print("\nLottery numbers:", lottery_numbers)
print("Your numbers:", user_numbers)
print("Correct numbers:", correct)
print("Points earned:", points)


# SEMINAR 14------------------------------------------------------------------------------------------------------------------------------


# 1. Based on the Student Grade class assignment from previous weeks, implement all the functionalities of the program we have added so far using functions.


def calculate_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    elif score >= 50:
        return "E"
    else:
        return "F"


def input_students():
    names = []
    scores = []
    grades = []

    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == "done":
            break

        score = float(input("Enter score: "))
        grade = calculate_grade(score)

        names.append(name)
        scores.append(score)
        grades.append(grade)

    return names, scores, grades


def display_students(names, grades):
    for i in range(len(names)):
        print(names[i], "-", grades[i])


def sort_students(names, scores):
    students = list(zip(names, scores))
    students.sort(key=lambda x: x[1], reverse=True)
    return students


def highest_student(names, scores):
    max_score = scores[0]
    index = 0

    for i in range(len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            index = i

    print("Congratulations", names[index] + "!")
    print("Highest score:", max_score)


# this is the main program
names, scores, grades = input_students()

print("\nStudents and grades:")
display_students(names, grades)

print("\nSorted by score (descending):")
sorted_students = sort_students(names, scores)
for s in sorted_students:
    print(s[0], "-", s[1])

highest_student(names, scores)



# 2. Create a function that takes a year and a month as parameters and returns the number of days in that month.

def days_in_month(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28
    else:
        return "Invalid month"


print(days_in_month(2024, 2))  # here is an example


# 3. Create a function that takes a year, month and date as parameters and returns what day of the week that day is


def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + (13 * (month + 1)) // 5 + k + (k // 4) + (j // 4) + (5 * j)) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]


print(day_of_week(2026, 1, 26))  # here is an example


# 4. Write a function that takes one number as parameter and returns True of False whether the number is prime or not

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


print(is_prime(17))  # True
print(is_prime(20))  # False

