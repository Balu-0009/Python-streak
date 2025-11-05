1# Program to check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

2# Program to find the prime numbers or not

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


3# Program to find the factorial of a number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

4# Program to generate Fibonacci series

num = int(input("Enter a number: "))

# Convert number to string to count digits
digits = len(str(num))

# Calculate the sum of digits raised to the power of number of digits
sum_of_powers = sum(int(digit) ** digits for digit in str(num))

# Check if Armstrong number
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


5# Program to check using srting methods

# Simple Python program using strings

# Taking a string variable
name = "PythonProgramming"

# Printing the string
print("Name:", name)

# String length
print("Length of the string:", len(name))

# Accessing characters in a string
print("First character:", name[0])
print("Last character:", name[-1])

# String concatenation
greeting = "Hello " + name
print(greeting)

# Changing string case
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())



  


