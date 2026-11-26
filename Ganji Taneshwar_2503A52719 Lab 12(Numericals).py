#q1
#Given the sorted array:
#A = [5, 10, 15, 20, 25, 30, 35, 40, 45]
#Apply Binary Search to find the key 30.
#Find:
#1. The values of low, high, and mid at each iteration.
#2. The middle element checked in each iteration.
#3. The final position of the key (using 0-based indexing).
#4. The total number of comparisons.

# Binary Search Implementation
'''def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        print(f"Iteration: low={low}, high={high}, mid={mid}, middle_element={arr[mid]}")
        
        if arr[mid] == key:
            print(f"Key {key} found at index {mid}. Total comparisons: {comparisons}")
       def     return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons
# Given sorted array
A = [5, 10, 15, 20, 25, 30, 35, 40, 45]     
# Key to search
key = 30
# Perform binary search
index, total_comparisons = binary_search(A, key)'''

#q2
#Given the sorted array:
#A = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
#Apply Binary Search to search for the key 50.
#Find:
#1. The values of low, high, and mid at each iteration.
#2. The elements compared with the key.
#3. The final result when the key is not present.
#4. The total number of comparisons.
      


# Binary Search Implementation
''' binary_search(arr, key):    
    
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        print(f"Iteration: low={low}, high={high}, mid={mid}, middle_element={arr[mid]}")
        
        if arr[mid] == key:
            print(f"Key {key} found at index {mid}. Total comparisons: {comparisons}")
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons

# Given sorted array
A = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66]
# Key to search 
key = 50
# Perform binary search     
index, total_comparisons = binary_search(A, key)  '''                                          

#q3
#Given the sorted array:
#A = [8, 16, 24, 32, 40, 48, 56, 64, 72]
#Apply Binary Search to find the key 8.
#Find:
#1. The low, high, and mid values in each iteration.
#2. The elements checked.
#3. The index of the key.
#4. The number of comparisons required.
        
         
# Binary Search Implementation
'''def binary_search(arr, key):    
    
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        print(f"Iteration: low={low}, high={high}, mid={mid}, middle_element={arr[mid]}")
        
        if arr[mid] == key:
            print(f"Key {key} found at index {mid}. Total comparisons: {comparisons}")
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons  

# Given sorted array
A = [8, 16, 24, 32, 40, 48, 56, 64, 72]
# Key to search         
key = 8
# Perform binary search 
index, total_comparisons = binary_search(A, key)'''

#q4
#Given the sorted array:
#A = [3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59]
#Apply Binary Search to find the key 47.
#Find:
#1. The low, high, and mid values at each iteration.
#2. The elements checked at each step.
#3. The final index of the key.
#4. The total number of comparisons.
       

# Binary Search Implementation
'''def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        print(f"Iteration: low={low}, high={high}, mid={mid}, middle_element={arr[mid]}")
        
        if arr[mid] == key:
            print(f"Key {key} found at index {mid}. Total comparisons: {comparisons}")
            return mid, comparisons
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons

# Given sorted array
A = [3, 7, 11, 15, 19, 23 , 27, 31, 35, 39, 43, 47, 51, 55, 59]
# Key to search
key = 47
# Perform binary search
index, total_comparisons = binary_search(A, key)'''


#q5
#Given the sorted array:
#A = [10, 20, 20, 20, 30, 40, 50, 60, 70]
#Apply a modified Binary Search to find the first occurrence of key 20.
#Find:
#1. The low, high, and mid values at each iteration.
#2. How the search continues after finding the key.
#3. The index of the first occurrence of 20.
#4. The total number of iterations.


# Modified Binary Search Implementation
'''def modified_binary_search(arr, key):       
    
    low = 0
    high = len(arr) - 1
    comparisons = 0
    first_occurrence_index = -1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        print(f"Iteration: low={low}, high={high}, mid={mid}, middle_element={arr[mid]}")
        
        if arr[mid] == key:
            first_occurrence_index = mid
            high = mid - 1  # Continue searching in the left half for the first occurrence
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    if first_occurrence_index != -1:
        print(f"First occurrence of key {key} found at index {first_occurrence_index}. Total comparisons: {comparisons}")
    else:
        print(f"Key {key} not found. Total comparisons: {comparisons}")
    
    return first_occurrence_index, comparisons

# Given sorted array
A = [10, 20, 20, 20, 30, 40, 50, 60, 70]
# Key to search     
key = 20
# Perform modified binary search
index, total_comparisons = modified_binary_search(A, key)'''

#q6
#Given the array:
#A = [45, 20, 35, 10, 55, 60]
#Apply Linear Search to find the key 45.
#Find:
#1. The elements checked.
#2. The index of the key.
#3. The number of comparisons required.
#4. The best-case time complexity.


                
# Linear Search Implementation
'''def linear_search(arr, key):    
    comparisons = 0

    for index, element in enumerate(arr):
        comparisons += 1
        print(f"Checking element: {element} at index {index}")
        
        if element == key:
            print(f"Key {key} found at index {index}. Total comparisons: {comparisons}")
            return index, comparisons

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons

# Given array
A = [45, 20, 35, 10, 55, 60]
# Key to search 
key = 45
# Perform linear search
index, total_comparisons = linear_search(A, key)'''



#q7
#Given the array:
#A = [11, 22, 33, 44, 55, 66, 77, 88]
#Apply Linear Search to find the key 88.
#Find:
#1. The order in which elements are checked.
#2. The index of the key.
#3. The total number of comparisons.
#4. The worst-case time complexity in terms of \(n\).
                    
                       

# Linear Search Implementation
def linear_search(arr, key):   
    comparisons = 0

    for index, element in enumerate(arr):
        comparisons += 1
        print(f"Checking element: {element} at index {index}")
        
        if element == key:
            print(f"Key {key} found at index {index}. Total comparisons: {comparisons}")
            return index, comparisons

    print(f"Key {key} not found. Total comparisons: {comparisons}")
    return -1, comparisons  

# Given array
A = [11, 22, 33, 44, 55, 66 , 77, 88]
# Key to search     
key = 88
# Perform linear search     
index, total_comparisons = linear_search(A, key)

