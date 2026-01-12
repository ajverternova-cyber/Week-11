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
