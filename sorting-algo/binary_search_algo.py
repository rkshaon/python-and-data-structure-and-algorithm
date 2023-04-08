# The basic steps to perform Binary Search are:
# 1. Sort the array in ascending order.
# 2. Set the low index to the first element of the array and the high index to the last element.
# 3. Set the middle index to the average of the low and high indices.
# 4. If the element at the middle index is the target element, return the middle index.
# 5. If the target element is less than the element at the middle index, set the high index to the middle index – 1.
# 6. If the target element is greater than the element at the middle index, set the low index to the middle index + 1.
# 7. Repeat steps 3-6 until the element is found or it is clear that the element is not present in the array.

# Binary Search Algorithm can be implemented in the following two ways
# 1. Iterative Method
# 2. Recursive Method

# 1. Iterative Method Binary Search Algorithm:
# binarySearch(arr, x, low, high)
#     repeat till low = high
#         mid = (low + high)/2
#             if (x == arr[mid]) 
#                   return mid
#             else if (x > arr[mid])    // x is on the right side
#                   low = mid + 1
#             else                      // x is on the left side
#                   high = mid - 1

# 2. Recursive Method (The recursive method follows the divide and conquer approach) Binary Search Algorithm:
# binarySearch(arr, x, low, high)
#     if low > high
#         return False 
#     else
#         mid = (low + high) / 2 
        
#         if x == arr[mid]
#             return mid
#         else if x > arr[mid]          // x is on the right side
#             return binarySearch(arr, x, mid + 1, high)
#         else                          // x is on the left side
#             return binarySearch(arr, x, low, mid - 1) 

# Iterative method
def binarySearchIterative(v, To_Find):
    lo = 0
    hi = len(v) - 1
 
    # This below check covers all cases , so need to check
    # for mid=lo-(hi-lo)/2
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
 
    if v[lo] == To_Find:
        print("Found At Index", lo)
    elif v[hi] == To_Find:
        print("Found At Index", hi)
    else:
        print("Not Found")

# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
            
#     return -1


# Recursive method
def binarySearchRecursive(arr, l, r, x):
    # Check base case
    if r >= l:
        mid = l + (r - l) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearchRecursive(arr, l, mid-1, x)
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearchRecursive(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1

# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
 
# Function call
binarySearchIterative(v=arr, To_Find=x)

result = binarySearchRecursive(arr, 0, len(arr)-1, x)
 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
