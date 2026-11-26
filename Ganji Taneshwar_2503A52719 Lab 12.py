#q1
#Linear Search Implementation with AI Assistance
#Task: generate a Python program that implements the Linear Search algorithm.
#Instructions:
#Prompt AI to create a function linear_search(arr, target) that searches for a target element in a list.
#Return the index of the target element if found; otherwise, return -1.
#include a docstring explaining the best-case, average-case, andworst-case time complexities.
#Test the function with different inputs, including an empty list and a target that is not present.
#Expected Output:
#A working Python program implementing Linear Search.
#Test cases with outputs.
#A brief explanation of time complexity.
              


'''def linear_search(arr, target):
    """
    Perform a linear search for the target element in the given list.

    Parameters:
    arr (list): The list to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the first position.
    - Average-case: O(n) - The target is found after checking half of the elements on average.
    - Worst-case: O(n) - The target is not present or is found at the last position.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
#Test cases
if __name__ == "__main__":
    # Test case 1: Target is present in the list
    arr1 = [5, 3, 8, 6, 2]
    target1 = 6
    print(f"Test case 1: Searching for {target1} in {arr1} -> Index: {linear_search(arr1, target1)}")  # Expected output: Index: 3

    # Test case 2: Target is not present in the list
    arr2 = [10, 20, 30, 40]
    target2 = 25
    print(f"Test case 2: Searching for {target2} in {arr2} -> Index: {linear_search(arr2, target2)}")  # Expected output: Index: -1

    # Test case 3: Empty list
    arr3 = []
    target3 = 5
    print(f"Test case 3: Searching for {target3} in {arr3} -> Index: {linear_search(arr3, target3)}")  # Expected output: Index: -1

    # Test case 4: Target is the first element
    arr4 = [7, 9, 11, 13]
    target4 = 7
    print(f"Test case 4: Searching for {target4} in {arr4} -> Index: {linear_search(arr4, target4)}")  # Expected output: Index: 0

    # Test case 5: Target is the last element
    arr5 = [1, 2, 3, 4, 5]
    target5 = 5
    print(f"Test case 5: Searching for {target5} in {arr5} -> Index: {linear_search(arr5, target5)}")  # Expected output: Index: 4'''

#q2
#Binary Search Implementation with AI Optimization
#Task: Use AI to generate an efficient Python program that implements Binary Search on a sorted list.
#Instructions:Prompt AI to create a function binary_search(arr, target).Use the iterative approach to find the target element.Return the index if the element is found; otherwise, return -1.Ask AI to explain why the input list must be sorted.Include best-case, average-case, and worst-case time complexities.Test the program with the first element, last element, middle element, and a missing element.
#Expected Output:A working Binary Search program.Test results for different target values.An explanation of why Binary Search is more efficient than Linear Search for large, sorted lists.




'''def binary_search(arr, target):     
    """
    Perform a binary search for the target element in the given sorted list.

    Parameters:
    arr (list): The sorted list to search through.
    target: The element to search for.

    Returns:
    int: The index of the target element if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the middle position.
    - Average-case: O(log n) - The search space is halved with each iteration.
    - Worst-case: O(log n) - The target is not present or is found at the last position.

    Note:
    Binary Search requires the input list to be sorted because it relies on the property that elements are ordered. This allows the algorithm to eliminate half of the search space in each iteration, making it more efficient than Linear Search for large datasets.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Test cases
if __name__ == "__main__":
    # Test case 1: Target is the first element
    arr1 = [10, 20, 30, 40, 50]
    target1 = 10
    print(f"Test case 1: Searching for {target1} in {arr1} -> Index: {binary_search(arr1, target1)}")  # Expected output: Index: 0

    # Test case 2: Target is the last element
    arr2 = [5, 15, 25, 35, 45]
    target2 = 45
    print(f"Test case 2: Searching for {target2} in {arr2} -> Index: {binary_search(arr2, target2)}")  # Expected output: Index: 4

    # Test case 3: Target is the middle element
    arr3 = [1, 3, 5, 7, 9]
    target3 = 5
    print(f"Test case 3: Searching for {target3} in {arr3} -> Index: {binary_search(arr3, target3)}")  # Expected output: Index: 2

    # Test case 4: Target is not present in the list
    arr4 = [2, 4, 6, 8, 10]
    target4 = 7
    print(f"Test case 4: Searching for {target4} in {arr4} -> Index: {binary_search(arr4, target4)}")  # Expected output: Index: -1 '''

#q3
#Student Record Search System
#Scenario: A university maintains student records containing roll numbers, names, and marks. Faculty members need to search for student records using roll numbers.
#Student Task:Use AI to recommend either Linear Search or Binary Search for searching student roll numbers.Implement both algorithms in Python.Test the algorithms using a list of student roll numbers.Compare the results when the roll numbers are stored in unsorted and sorted order.Explain the time complexity of both algorithms.
#Expected Output:Python functions for Linear Search and Binary Search.Sample student records and test results.A comparison table showing algorithm, input requirements, and time complexity.Justification for selecting the appropriate search algorithm.

'''def linear_search(arr, target):
    """
    Perform a linear search for the target roll number in the given list.

    Parameters:
    arr (list): The list of student roll numbers to search through.
    target: The roll number to search for.

    Returns:
    int: The index of the target roll number if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the first position.
    - Average-case: O(n) - The target is found after checking half of the elements on average.
    - Worst-case: O(n) - The target is not present or is found at the last position.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1   


def binary_search(arr, target):
    """
    Perform a binary search for the target roll number in the given sorted list.

    Parameters:
    arr (list): The sorted list of student roll numbers to search through.
    target: The roll number to search for.

    Returns:
    int: The index of the target roll number if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the middle position.
    - Average-case: O(log n) - The search space is halved with each iteration.
    - Worst-case: O(log n) - The target is not present or is found at the last position.

    Note:
    Binary Search requires the input list to be sorted because it relies on the property that elements are ordered. This allows the algorithm to eliminate half of the search space in each iteration, making it more efficient than Linear Search for large datasets.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1           



#test cases
if __name__ == "__main__":  
        
    # Sample student roll numbers
    unsorted_roll_numbers = [102, 101, 104, 103, 105]
    sorted_roll_numbers = sorted(unsorted_roll_numbers)

    # Test case 1: Searching in unsorted list using Linear Search
    target1 = 103
    index1 = linear_search(unsorted_roll_numbers, target1)
    print(f"Linear Search (Unsorted): Searching for {target1} in {unsorted_roll_numbers} -> Index: {index1}")  # Expected output: Index: 3

    # Test case 2: Searching in sorted list using Binary Search
    target2 = 104
    index2 = binary_search(sorted_roll_numbers, target2)
    print(f"Binary Search (Sorted): Searching for {target2} in {sorted_roll_numbers} -> Index: {index2}")  # Expected output: Index: 3

    # Test case 3: Searching for a non-existent roll number
    target3 = 106
    index3_linear = linear_search(unsorted_roll_numbers, target3)
    index3_binary = binary_search(sorted_roll_numbers, target3)
    print(f"Linear Search (Unsorted): Searching for {target3} -> Index: {index3_linear}")  # Expected output: Index: -1
    print(f"Binary Search (Sorted): Searching for {target3} -> Index: {index3_binary}")  # Expected output: Index: -1
            '''

#Task Description #4: Library Book Search System
#Scenario: A college library maintains a list of book identification numbers. Students and librarians need to find books quickly using their book IDs.
#Student Task:Use AI to generate a Python program that searches for a book ID using Linear Search.Implement Binary Search to search for the same book ID in a sorted list.Test both algorithms when the book ID exists and when it does not exist.Measure and compare the number of comparisons performed by each algorithm.Ask AI to explain which algorithm is suitable for a large, sorted collection of book IDs.
#Expected Output:Working Python programs for both searching algorithms.Test cases with search results.A comparison of the number of comparisons performed.A conclusion explaining the efficiency of each algorithm

'''def linear_search(arr, target):
    """
    Perform a linear search for the target book ID in the given list.

    Parameters:
    arr (list): The list of book IDs to search through.
    target: The book ID to search for.

    Returns:
    int: The index of the target book ID if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the first position.
    - Average-case: O(n) - The target is found after checking half of the elements on average.
    - Worst-case: O(n) - The target is not present or is found at the last position.
    """
    comparisons = 0
    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            print(f"Linear Search Comparisons: {comparisons}")
            return index
    print(f"Linear Search Comparisons: {comparisons}")
    return -1


def binary_search(arr, target):
    """
    Perform a binary search for the target book ID in the given sorted list.

    Parameters:
    arr (list): The sorted list of book IDs to search through.
    target: The book ID to search for.

    Returns:
    int: The index of the target book ID if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the middle position.
    - Average-case: O(log n) - The target is found after checking half of the remaining elements on average.
    - Worst-case: O(log n) - The target is not present or is found at the first or last position.
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Binary Search Comparisons: {comparisons}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Binary Search Comparisons: {comparisons}")
    return -1

#test cases
if __name__ == "__main__":  
    
    # Sample book IDs
    unsorted_book_ids = [1005, 1001, 1003, 1002, 1004]
    sorted_book_ids = sorted(unsorted_book_ids)

    # Test case 1: Searching in unsorted list using Linear Search
    target1 = 1003
    index1 = linear_search(unsorted_book_ids, target1)
    print(f"Linear Search (Unsorted): Searching for {target1} in {unsorted_book_ids} -> Index: {index1}")  # Expected output: Index: 2

    # Test case 2: Searching in sorted list using Binary Search
    target2 = 1004
    index2 = binary_search(sorted_book_ids, target2)
    print(f"Binary Search (Sorted): Searching for {target2} in {sorted_book_ids} -> Index: {index2}")  # Expected output: Index: 3

    # Test case 3: Searching for a non-existent book ID
    target3 = 1006
    index3_linear = linear_search(unsorted_book_ids, target3)
    index3_binary = binary_search(sorted_book_ids, target3)
    print(f"Linear Search (Unsorted): Searching for {target3} -> Index: {index3_linear}")  # Expected output: Index: -1
    print(f"Binary Search (Sorted): Searching for {target3} -> Index: {index3_binary}")  # Expected output: Index: -1'''



#Task Description #5: Searching Algorithm Comparison and Optimization
#Scenario: An online shopping platform maintains product IDs for thousands of products. The system must locate a product quickly when a customer enters a product ID.
#Student Task:Use AI to generate Python implementations of Linear Search and Binary Search.Test both algorithms using the same collection of product IDs.Compare the execution time and number of comparisons for different input sizes.Test the algorithms with the first element, middle element, last element, and an element that does not exist.Ask AI to suggest optimizations and explain the limitations of each algorithm.Present the results in a table and justify which algorithm is appropriate for sorted product IDs.
#Expected Output:Python implementations of both algorithms.Test results for different input sizes.A comparison table containing execution time, number of comparisons, and time complexity.A brief conclusion based on the experimental results.

def linear_search(arr, target):
    """
    Perform a linear search for the target product ID in the given list.

    Parameters:
    arr (list): The list of product IDs to search through.
    target: The product ID to search for.

    Returns:
    int: The index of the target product ID if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the first position.
    - Average-case: O(n) - The target is found after checking half of the elements on average.
    - Worst-case: O(n) - The target is not present or is found at the last position.
    """
    comparisons = 0
    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            print(f"Linear Search Comparisons: {comparisons}")
            return index
    print(f"Linear Search Comparisons: {comparisons}")
    return -1


def binary_search(arr, target): 
    """
    Perform a binary search for the target product ID in the given sorted list.

    Parameters:
    arr (list): The sorted list of product IDs to search through.
    target: The product ID to search for.

    Returns:
    int: The index of the target product ID if found; otherwise, -1.

    Time Complexity:
    - Best-case: O(1) - The target is found at the middle position.
    - Average-case: O(log n) - The target is found after checking half of the remaining elements on average.
    - Worst-case: O(log n) - The target is not present or is found at the first or last position.

    Note:
    Binary Search requires the input list to be sorted because it relies on the property that elements are ordered. This allows the algorithm to eliminate half of the search space in each iteration, making it more efficient than Linear Search for large datasets.
    """
    comparisons = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            print(f"Binary Search Comparisons: {comparisons}")
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Binary Search Comparisons: {comparisons}")
    return -1

#test cases
if __name__ == "__main__":
    # Sample product IDs
    unsorted_product_ids = [2005, 2001, 2003, 2002, 2004]
    sorted_product_ids = sorted(unsorted_product_ids)

    # Test case 1: Searching in unsorted list using Linear Search
    target1 = 2003
    index1 = linear_search(unsorted_product_ids, target1)
    print(f"Linear Search (Unsorted): Searching for {target1} in {unsorted_product_ids} -> Index: {index1}")  # Expected output: Index: 2

    # Test case 2: Searching in sorted list using Binary Search
    target2 = 2004
    index2 = binary_search(sorted_product_ids, target2)
    print(f"Binary Search (Sorted): Searching for {target2} in {sorted_product_ids} -> Index: {index2}")  # Expected output: Index: 3

    # Test case 3: Searching for a non-existent product ID
    target3 = 2006
    index3_linear = linear_search(unsorted_product_ids, target3)
    index3_binary = binary_search(sorted_product_ids, target3)
    print(f"Linear Search (Unsorted): Searching for {target3} -> Index: {index3_linear}")  # Expected output: Index: -1
    print(f"Binary Search (Sorted): Searching for {target3} -> Index: {index3_binary}")  # Expected output: Index: -1

    








                                        








                            
















   
         

    