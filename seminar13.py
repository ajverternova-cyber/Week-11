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


