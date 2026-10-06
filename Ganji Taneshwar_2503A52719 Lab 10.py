"""Calculate and display a student's average score."""


'''def calc_average(marks):
	"""Return the arithmetic mean of the given marks."""
	if not marks:
		raise ValueError("marks must contain at least one score")

	total = 0
	for mark in marks:
		total += mark
	average = total / len(marks)
	return average


marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))

# Fixes: restored the missing indentation, removed unrelated "Week5 - Monday"
# text, corrected the return variable typo, and closed the print call properly.
# The empty-list check also prevents division by zero.



"""Calculate and display the area of a rectangle."""


def area_of_rect(length, breadth):
    """Return the area of a rectangle."""
    return length * breadth


print(area_of_rect(10, 20))

#q3
def calculate_percentage(value, percentage):
	"""Return the requested percentage of a value."""
	return value * percentage / 100


amount = 200
percentage_rate = 15
print(calculate_percentage(amount, percentage_rate))'''


'''# Find squares of numbers efficiently with a list comprehension.
nums = range(1, 1_000_000)
squares = [n * n for n in nums]
print(len(squares))'''


def grade(score):
	"""Return the letter grade for a numeric score."""
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	return "F"
print(grade(85))  # Output: B
print(grade(72))  # Output: C







