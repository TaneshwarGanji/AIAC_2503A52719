#Q1
#Write a Python function to check whether a given number is a palindrome  
'''def is_palindrome(n):
    # Convert the number to string
    str_n = str(n)
    # Check if the string is equal to its reverse
    return str_n == str_n[::-1]
# Test the function
test_number = 121               
if is_palindrome(test_number):
    print(f"{test_number} is a palindrome.")
else:
    print(f"{test_number} is not a palindrome.")'''
#Write a Python function that accepts a number as input and checks whether the number is a palindrome. Return "Palindrome" if the number reads the same forwards and backwards otherwise return "Not a Palindrome"
'''def check_palindrome(n):
    str_n = str(n)
    if str_n == str_n[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"
# Test the function
test_number = 12321     
result = check_palindrome(test_number)
print(f"{test_number} is {result}.")'''   
#Q2
#Write a Python function to calculate the factorial of a given non-negative integer.Example:Input:5,Output:120.Based on this example generate a clear and correct Python function that accepts an integer and returns its factorial.
'''def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
    # Test the function
test_number = 5     
result = calculate_factorial(test_number)
print(f"The factorial of {test_number} is {result}.")'''
#Q3
#Write a Python function that checks whether a given integer is an Armstrong number.Examples:Input: 153 → Output: Armstrong Number,Input: 370 → Output: Armstrong Number and Input: 123 → Output: Not an Armstrong Number.Based on these examples generate a Python function that correctly checks Armstrong numbers. Handle zero, negative numbers and invalid inputs appropriately.
'''def is_armstrong_number(n):
    # Check if the input is a valid integer
    if not isinstance(n, int):
        return "Invalid input. Please enter an integer."
    
    # Handle negative numbers
    if n < 0:
        return "Not an Armstrong Number"
    
    # Calculate the number of digits
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate the sum of the digits raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    if sum_of_powers == n:
        return "Armstrong Number"
    else:
        return "Not an Armstrong Number"
# Test the function
test_numbers = [153, 370, 123, -5, 0, 'abc']
for number in test_numbers:
    result = is_armstrong_number(number)
    print(f"{number}: {result}")'''
#Q4
#Write an optimized Python program that accepts an integer and classifies it as:Prime,Composite and Neither.Requirements:A prime number has exactly two positive factors: 1 and itself.A composite number has more than two positive factors.0 and 1 must be classified as Neither.Negative numbers must be rejected as invalid input.Non-integer input must be handled properly.For efficiency, check divisibility only up to the square root of the number.Give clear output messages.Use a separate function for classification.
'''def classify_number(n):
    # Check if the input is a valid integer
    if not isinstance(n, int):
        return "Invalid input. Please enter an integer."
    
    # Handle negative numbers
    if n < 0:
        return "Invalid input. Negative numbers are not allowed."
    
    # Classify the number
    if n == 0 or n == 1:
        return "Neither"
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Composite"
    
    return "Prime"
# Test the function
test_numbers = [0, 1, 2, 3, 4, 5, 16, 17, -5, 'abc']
for number in test_numbers:
    result = classify_number(number)
    print(f"{number}: {result}")'''  
#Q5
#Write a Python function that checks whether a given positive integer is a perfect number.A perfect number is a number whose positive divisors excluding the number itself add up to the number.Return True if the number is a perfect number and False otherwise.
'''def is_perfect_number(n):
    # Check if the input is a valid positive integer
    if not isinstance(n, int) or n <= 0:
        return "Invalid input. Please enter a positive integer."
    
    # Calculate the sum of divisors excluding the number itself
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    
    # Check if the sum of divisors is equal to the original number
    return sum_of_divisors == n
# Test the function
test_numbers = [6, 28, 12, 496, 8128, -5, 0, 'abc']
for number in test_numbers: 
    result = is_perfect_number(number)
    print(f"{number}: {result}")'''
#Q6
#Write a Python program that determines whether a given number is even or odd and includes proper input validation.Use these examples as guidance:Input: 8 and Output: Even,Input: 15 and Output: Odd,Input: 0 and Output: Even.Requirements:1. Accept only integer input.2. Positive and negative integers should be handled.3. Zero should be classified as Even.4. Display "Even" or "Odd" as the output.5. Display a clear error message for non-integer input.6. Keep the program simple and easy to understand.
'''def check_even_odd(n):
    # Check if the input is a valid integer
    if not isinstance(n, int):
        return "Invalid input. Please enter an integer."
    
    # Check if the number is even or odd
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"    
# Test the function
test_numbers = [8, 15, 0, -4, -7, 'abc']
for number in test_numbers:
    result = check_even_odd(number)
    print(f"{number}: {result}")'''
