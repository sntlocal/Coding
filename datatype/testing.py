# This is a simple Python program that greets you and does basic math

# 1. Print a message to the console
print("Hello! Welcome to Python.")

# 2. Use variables and take user input
name = input("What is your name? ")
print(f"It's nice to meet you, {name}!")

# 3. Perform a simple calculation
num1 = 10
num2 = 5
result = num1 + num2

# 4. Use a conditional statement
if result > 10:
    print(f"The sum of {num1} and {num2} is {result}, which is greater than 10.")
else:
    print(f"The sum is {result}.")

# 5. Use a simple loop
print("Counting to 3:")
for i in range(1, 4):
    print(i)
