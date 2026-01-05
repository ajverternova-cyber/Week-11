#This is Week 10
print("Hello")
print("This is a simple calculator")
print("Hello", "Hello")
num1 = 4
num2 = 5+5
name = "student"
result = num1 + num2
print(num1, num2, name, result)
#Taking input from the user.
age = int(input("What is your age?"))

if age > 10:
    print("You pay 200 ALL")
elif age > 18:
    print("You pay 500 ALL")
else:
    print("You have it for free.")
#Conditional Statements
if age < 0:
    print("You aren't born yet.")
elif age >= 18:
    print("You are an adult")
else:
    print("You are a child")
