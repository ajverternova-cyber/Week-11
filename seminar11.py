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
