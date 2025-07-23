#Python code to try Math 
# Addition, subtraction, multiplication, and division
a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
# Check if a number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Function to calculate square
def square(num):
    return num * num

# Call the function
result = square(number)
print("Square of", number, " is:", result)

