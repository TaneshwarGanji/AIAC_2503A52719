#write a python programming code to generate fibonacci series
def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Example usage
n = int(input("Enter the number of terms in the Fibonacci series: "))   
print(f"The first {n} terms of the Fibonacci series are: {fibonacci_series(n)}")
#generate a python code for alphabetic numbers
def alphabetic_numbers(n):
    alphabetic_list = []
    for i in range(1, n + 1):
        alphabetic_list.append(str(i))
    return alphabetic_list
# Example usage
n = int(input("Enter a number to generate alphabetic numbers: "))   
print(f"The alphabetic numbers up to {n} are: {alphabetic_numbers(n)}")
#generate a python code for vowels
def vowels_in_string(s):
    vowel_list = []
    for char in s:
        if char.lower() in "aeiou":
            vowel_list.append(char)
    return vowel_list
# Example usage
s = input("Enter a string to find vowels: ")
print(f"The vowels in '{s}' are: {vowels_in_string(s)}")
