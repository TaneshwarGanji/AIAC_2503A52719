#q1
n = int(input("Enter N: "))

for i in range(2, n + 1, 2):
    print(i)
#q2
numbers = [12, 15, 18, 21, 24, 27]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
#q3
#Generate a Python class User that validates age and email using conditional statements
class User:
    def __init__(self, age, email):
        self.age = age
        self.email = email

    def validate_age(self):
        if self.age < 0:
            return "Age cannot be negative."
        elif self.age < 18:
            return "User is a minor."
        else:
            return "User is an adult."

    def validate_email(self):
        if "@" in self.email and "." in self.email:
            return "Email is valid."
        else:
            return "Email is invalid."
#testing the User class
user1 = User(25, "user@example.com")
print(user1.validate_age())
print(user1.validate_email())
#q4
#Generate a Python class Student with attributes (name, roll number, marks) and methods to calculate total and average marks.
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)
#testing the Student class
student1 = Student("Alice", 101, [85, 90, 78])  
print("Total marks:", student1.calculate_total())
print("Average marks:", student1.calculate_average())
#q5
#Generate a Python program for a simple bank account system using class, loops, and conditional statements.
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")
#testing the BankAccount class
account1 = BankAccount("123456", "John Doe", 1000)
print("Initial balance:")
account1.display_balance()  
account1.deposit(500)
account1.withdraw(200)  



