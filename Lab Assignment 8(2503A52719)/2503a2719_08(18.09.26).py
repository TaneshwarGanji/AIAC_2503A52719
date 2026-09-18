'''def is_strong_password(password):
    """Return True if password satisfies strength requirements."""
    if password is None:
        return False
    if len(password) < 8:
        return False
    if " " in password:
        return False

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

    return has_upper and has_lower and has_digit and has_special


# Assert test cases
assert is_strong_password("Abcdef1!") is True
assert is_strong_password("abcde1!") is False  # too short
assert is_strong_password("abcdefgh") is False  # missing uppercase, digit, special
assert is_strong_password("Abcdef gh1!") is False  # contains space
assert is_strong_password("NoSpace123!") is True
assert is_strong_password("Password123") is False  # missing special character
print("Task 1: All tests passed!")'''
'''def classify_number(n):
    """Return the classification of an integer value."""
    if n is None or isinstance(n, (str, float, bool, complex)):
        return "Invalid"

    checks = [
        ("Negative", n < 0),
        ("Zero", n == 0),
        ("Positive", n > 0),
    ]

    for label, condition in checks:
        if condition:
            return label

    return "Invalid"


# Boundary and normal cases
assert classify_number(10) == "Positive"
assert classify_number(-5) == "Negative"
assert classify_number(0) == "Zero"
assert classify_number(-1) == "Negative"
assert classify_number(1) == "Positive"

# Invalid input handling
assert classify_number("abc") == "Invalid"
assert classify_number(None) == "Invalid"
assert classify_number(3.14) == "Invalid"

print("Task 2: Classification logic passing all assert tests.")'''


'''def is_anagram(str1, str2):
    """Return True if two strings are anagrams when ignoring case, spaces, and punctuation."""
    if str1 is None or str2 is None:
        return False

    normalized1 = ''.join(ch.lower() for ch in str1 if ch.isalnum())
    normalized2 = ''.join(ch.lower() for ch in str2 if ch.isalnum())

    return sorted(normalized1) == sorted(normalized2)


# Assert test cases
assert is_anagram("listen", "silent") is True
assert is_anagram("hello", "world") is False
assert is_anagram("Dormitory", "Dirty Room") is True
assert is_anagram("", "") is True
assert is_anagram("A man, a plan, a canal: Panama", "Amanaplanacanalpanama") is True
assert is_anagram("abc", "abcd") is False

print("Task 3: Anagram checker passing all assert tests.")'''


'''class Inventory:
    """Simple stock management for inventory items."""

    def __init__(self):
        self.stock = {}

    def add_item(self, name, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")

        self.stock[name] = self.stock.get(name, 0) + quantity
        return self.stock[name]

    def remove_item(self, name, quantity):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if name not in self.stock:
            raise KeyError(f"Item '{name}' is not in stock.")
        if quantity > self.stock[name]:
            raise ValueError(f"Cannot remove {quantity} of '{name}'. Only {self.stock[name]} available.")

        self.stock[name] -= quantity
        if self.stock[name] == 0:
            del self.stock[name]

    def get_stock(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        return self.stock.get(name, 0)


# Task 4: Inventory class assert tests
inv = Inventory()
inv.add_item("Pen", 10)
assert inv.get_stock("Pen") == 10

inv.remove_item("Pen", 5)
assert inv.get_stock("Pen") == 5

inv.add_item("Book", 3)
assert inv.get_stock("Book") == 3

inv.add_item("Pen", 7)
assert inv.get_stock("Pen") == 12

inv.remove_item("Pen", 12)
assert inv.get_stock("Pen") == 0

assert inv.get_stock("Notebook") == 0

print("Task 4: Inventory class passing all assert tests.")'''

from datetime import datetime


'''def validate_and_format_date(date_str):
    """Validate MM/DD/YYYY input and convert it to YYYY-MM-DD."""
    if not isinstance(date_str, str):
        return "Invalid Date"

    try:
        parsed = datetime.strptime(date_str, "%m/%d/%Y")
    except ValueError:
        return "Invalid Date"

    return parsed.strftime("%Y-%m-%d")


# Task 5: Date validation and formatting assert tests
assert validate_and_format_date("10/15/2023") == "2023-10-15"
assert validate_and_format_date("02/30/2023") == "Invalid Date"  # invalid day
assert validate_and_format_date("01/01/2024") == "2024-01-01"
assert validate_and_format_date("12/31/1999") == "1999-12-31"
assert validate_and_format_date("13/01/2024") == "Invalid Date"  # invalid month
assert validate_and_format_date("2023-10-15") == "Invalid Date"  # wrong format

print("Task 5: Date validation and formatting assertions passed.")'''

