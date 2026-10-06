#q1
import io
from contextlib import redirect_stdout


def greet():
    print("Hello, AI Debugging Lab!")


# Corrected program
greet()


def capture_output():
    output = io.StringIO()
    with redirect_stdout(output):
        greet()
    return output.getvalue()


# Three assert test cases
assert capture_output() == "Hello, AI Debugging Lab!\n"
assert capture_output().strip() == "Hello, AI Debugging Lab!"
assert capture_output().startswith("Hello, AI Debugging Lab!")
#q2
# In Python, `=` is the assignment operator, not the comparison operator.
# Using `=` inside an `if` condition tries to assign a value to `n`,
# which causes a syntax error. The comparison operator should be `==`.

def check_number(n):
    if n == 10:
        return "Ten"
    else:
        return "Not Ten"
#test cases for the function
print(check_number(10))  # Expected output: "Ten"
print(check_number(5))   # Expected output: "Not Ten"
#q3

# Debugged file-reading program

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' was not found."
    except (OSError, ValueError):
        return f"Error: The path '{filename}' is invalid or cannot be accessed."
    except Exception as e:
        return f"Error: Something went wrong while reading '{filename}': {e}"


# Tests
# 1) Existing file
with open("existing.txt", "w", encoding="utf-8") as f:
    f.write("Hello from existing.txt\n")
print(read_file("existing.txt"))

# 2) Missing file
print(read_file("nonexistent.txt"))

# 3) Invalid path
print(read_file("bad\0name.txt"))
#q4

# The missing method should be defined, not the method call corrected.
# The class is missing a `drive` method, so we define it and then test it.

class Car:
    def start(self):
        return "Car started"

    def drive(self):
        return "Car is driving"


my_car = Car()

# Three assert tests
assert my_car.start() == "Car started"
assert my_car.drive() == "Car is driving"
assert my_car.drive().startswith("Car")
print(my_car.start())
print(my_car.drive())
print("All tests passed for Car class.")
#q5

# Solution 1: Type casting for numerical addition
# This converts the string input to an integer before adding 5.
def add_five_numeric(value):
    return int(value) + 5


# Solution 2: String concatenation
# This keeps the value as a string and appends the integer converted to a string.
def add_five_string(value):
    return value + str(5)


# Validate the corrected code with three assert tests
assert add_five_numeric("10") == 15
assert add_five_numeric("20") == 25
assert add_five_string("10") == "105"
print(add_five_numeric("10"))  # Expected output: 15
print(add_five_string("10"))   # Expected output: "105"
