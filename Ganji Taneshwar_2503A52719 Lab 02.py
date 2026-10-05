#You are evaluating AI tools for numeric validation logic.Generate an Armstrong number checker
'''An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because it has 3 digits and 1^3 + 5^3 + 3^3 = 153.
Here is a Python function that checks if a given number is an Armstrong number:'''
'''def is_armstrong_number(num):
    """Check if a number is an Armstrong number.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.

    Example:
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(123)
        False
    """
    # Convert the number to a string to easily iterate over digits
    digits = str(num)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the calculated sum is equal to the original number
    return armstrong_sum == num
# Example usage:
print(is_armstrong_number(153))  # Output: True 
print(is_armstrong_number(123))  # Output: False
print(is_armstrong_number(1652)) # Output: False   ''' 
#You are validating a calendar module for a backend system. generate a Python program that checks whether a given year is a leap year.
'''Here is a Python program that checks whether a given year is a leap year:'''
'''def is_leap_year(year):
    """Check if a year is a leap year.

    Args:
        year (int): The year to check.
    Returns:
        bool: True if the year is a leap year, False otherwise.
    Example:
        >>> is_leap_year(2020)
        True
        >>> is_leap_year(1900)
        False
        >>> is_leap_year(2000)
        True
    """
    # A year is a leap year if it is divisible by 4
    # but not divisible by 100, unless it is also divisible by 400.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Example usage:
print(is_leap_year(2020))  # Output: True   
print(is_leap_year(1900))  # Output: False
print(is_leap_year(2000))  # Output: True'''
#Company policy requires developers to write logic before using AI.Write a Python program that calculates the sum of odd and even numbers in a tuple.
'''Here is a Python program that calculates the sum of odd and even numbers in a tuple:'''
def sum_odd_even(numbers):           
    """Calculate the sum of odd and even numbers in a tuple.

    Args:
        numbers (tuple): A tuple of integers.

    Returns:
        tuple: A tuple containing the sum of even numbers and the sum of odd numbers.

    Example:
        >>> sum_odd_even((1, 2, 3, 4, 5))
        (6, 9)
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    
    return even_sum, odd_sum            
# Example usage:
print(sum_odd_even((1, 2, 3, 4, 5)))  # Output: (6, 9)
print(sum_odd_even((10, 15, 20, 25, 30)))  # Output: (60, 40)
print(sum_odd_even((0, 1, 2, 3, 4, 5)))  # Output: (6, 9)

                                                



