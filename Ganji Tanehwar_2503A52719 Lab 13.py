#q1
#A company maintains employee salary records. The system needs to arrange salaries in ascending order.Write a program to implement Insertion Sort.Explain the role of the key element and shifting operations. Display the array after each iteration.Analyze the algorithms efficiency for nearly sorted data.

#Here's a Python program that implements the Insertion Sort algorithm to arrange employee salaries in ascending order. The program also displays the array after each iteration and explains the role of the key element and shifting operations.```python
'''def insertion_sort(salaries):
    # Traverse through 1 to len(salaries)
    for i in range(1, len(salaries)):
        key = salaries[i]  # The key element is the current salary to be inserted
        j = i - 1
        
        # Move elements of salaries[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < salaries[j]:
            salaries[j + 1] = salaries[j]  # Shifting operation
            j -= 1
        
        salaries[j + 1] = key  # Insert the key element at the correct position
        
        # Display the array after each iteration
        print(f"Iteration {i}: {salaries}")
# Example usage
salaries = [50000, 60000, 55000, 70000, 65000]
print("Original salaries:", salaries)   
insertion_sort(salar# Example usage

print("Sorted salaries:", salaries)
# Efficiency Analysis:
# The Insertion Sort algorithm is efficient for nearly sorted data because it minimizes the number of comparisons and shifts required to sort the array. In the best-case scenario, where the data is already sorted, the algorithm runs in O(n) time complexity, as it only needs to make a single pass through the array without any shifting. In contrast, for completely unsorted data, the time complexity is O(n^2) due to the nested loops. Therefore, Insertion Sort is particularly effective for small datasets or datasets that are already partially sorted.'''
#q2
#A hospital maintains thousands of patient records containing PatientID, Patient Name, and Medical Bill Amount.Write a python program to implement Merge Sort to arrange patient records based on bill amount.Demonstrate the divide-and-conquer process.Show the splitting and merging operations.Analyze the time and space complexities.


'''def merge_sort(records):
    if len(records) > 1:
        mid = len(records) // 2  # Finding the mid of the array
        left_half = records[:mid]  # Dividing the elements into 2 halves
        right_half = records[mid:]

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i][2] < right_half[j][2]:  # Compare based on bill amount
                records[k] = left_half[i]
                i += 1
            else:
                records[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            records[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            records[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    # Example usage
    patient_records = [
        (101, "Alice", 500.0),
        (102, "Bob", 300.0),
        (103, "Charlie", 700.0),
        (104, "David", 400.0),
        (105, "Eve", 600.0)
    ]
    print("Original patient records:", patient_records)
    merge_sort(patient_records)
    print("Sorted patient records based on bill amount:", patient_records)
# Efficiency Analysis:
# The Merge Sort algorithm has a time complexity of O(n log n) in all cases (best, average, and worst) because it consistently divides the array into halves and merges them back together. The space complexity is O(n) due to the temporary arrays used for merging. This makes Merge Sort efficient for large datasets, especially when stability (preserving the order of equal elements) is required.      '''
#q3
#Selection Sort – Product Price Management.An online shopping platform maintains a list of product prices.Write a program to implement Selection Sort to arrange product prices in ascending order.Identify the minimum element in every pass.Display the array after each pass.Analyze the time and space complexities.
'''def selection_sort(prices):
    n = len(prices)
    for i in range(n):
        min_index = i  # Assume the minimum is the first element of the unsorted part
        for j in range(i + 1, n):
            if prices[j] < prices[min_index]:  # Find the minimum element in the remaining unsorted array
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        prices[i], prices[min_index] = prices[min_index], prices[i]
        
        # Display the array after each pass
        print(f"Pass {i + 1}: {prices}")
# Example usage
product_prices = [29.99, 19.99, 49.99, 9.99, 39.99]
print("Original product prices:", product_prices)   
selection_sort(product_prices)
print("Sorted product prices:", product_prices) 
# Efficiency Analysis:
# The Selection Sort algorithm has a time complexity of O(n^2) in all cases ( best, average, and worst) because it always requires two nested loops to find the minimum element. The space complexity is O(1) since it sorts the array in place without requiring additional storage. While Selection Sort is simple to implement, it is not efficient for large datasets compared to more advanced sorting algorithms.'''

#q4
#Bubble Sort – Student Marks Sorting
#A university maintains student records containing Roll Number,Student Name, and Marks.Write a program to implement Bubble Sort to arrange students in ascending order of marks.Display the array after each pass.Explain the swapping process.
'''def bubble_sort(students):
    n = len(students)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if students[j][2] > students[j + 1][2]:  # Compare marks
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        # Display the array after each pass
        print(f"Pass {i + 1}: {students}")
        if not swapped:  # If no swapping occurred, the array is sorted
            break

# Example usage
student_records = [
    (1, "Alice", 85),
    (2, "Bob", 92),
    (3, "Charlie", 78),
    (4, "David", 96),
    (5, "Eve", 88)
]
print("Original student records:", student_records)
bubble_sort(student_records)
print("Sorted student records based on marks:", student_records)

# Efficiency Analysis:
# The Bubble Sort algorithm has a time complexity of O(n^2) in the worst and average cases due to the nested loops required for comparisons and swaps. However, in the best-case scenario, where the data is already sorted, the time complexity is O(n) because it only requires a single pass through the array without any swaps. The space complexity is O(1) since it sorts the array in place without requiring additional storage. The swapping process involves exchanging the positions of two elements when they are out of order, which helps to "bubble" the larger elements to the end of the list with each pass.'''

#q5
#Sort – Examination Result Processing
#A university maintains examination results containing Roll Number,Student Name, and Total Marks.Write a python program to implement Quick Sort to arrange students in descending order of marks.Select the last element as the pivot.Explain the partitioning process and recursive calls.Analyze the best, average, and worst-case time complexities.

def quick_sort(students):
    if len(students) <= 1:
        return students
    else:
        pivot = students[-1]  # Select the last element as the pivot
        less_than_pivot = [student for student in students[:-1] if student[2] > pivot[2]]  # Students with marks greater than pivot
        greater_than_pivot = [student for student in students[:-1] if student[2] <= pivot[2]]  # Students with marks less than or equal to pivot
        
        # Recursive calls to sort the partitions
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
student_records = [
    (1, "Alice", 85),
    (2, "Bob", 92),
    (3, "Charlie", 78),
    (4, "David", 96),
    (5, "Eve", 88)
]

print("Original student records:", student_records)
sorted_records = quick_sort(student_records)
print("Sorted student records based on marks (descending):", sorted_records)

# Efficiency Analysis:
# The Quick Sort algorithm has a best and average-case time complexity of O(n log n)    
    




