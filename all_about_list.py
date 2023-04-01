# count(x) - Returns the number of occurrences of element x in the list.
# sort(key=None, reverse=False) - Sorts the list in ascending order. Optional arguments key and reverse allow customization of the sorting behavior.
# reverse() - Reverses the order of elements in the list.
# copy() - Returns a shallow copy of the list.

# What is List?
# In Python, a list is a built-in data structure that allows you to store 
# and organize a collection of items in a particular order. A list is an 
# ordered sequence of objects, where each object can be of any type, such 
# as integers, floats, strings, or other objects. Lists are created by 
# enclosing a comma-separated sequence of values within square brackets [ ].
# Example
# my_list = [1, 2, 3, 4, 5]
# Lists are mutable, which means you can add, remove, or modify elements after 
# the list has been created. You can access individual elements in a list by 
# their index, starting with 0 for the first element, and you can use slicing 
# to extract a subset of the list.

# append - Adds an element `x` to the end of the list.
my_list = [1, 2, 3, 4, 5]
my_list.append(10) # [1, 2, 3, 4, 5, 10]
# A single value required to append in a list
print(f"After append: {my_list}")

# extend - Adds elements from an iterable to the end of the list.
my_list = [1, 2, 3, 4, 5]
my_list.extend([10, 11, 12]) # [1, 2, 3, 4, 5, 10, 11, 12]
# Another list required to extend in a list
print(f"After extend: {my_list}")

# insert - Inserts element `x` at position `i` in the list.
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10) # [1, 2, 10, 3, 4, 5]
# An index and a value required to insert in a list
print(f"After insert: {my_list}")

# remove - Removes the first occurrence of element `x` from the list.
my_list = [1, 2, 3, 4, 5, 3]
my_list.remove(3) # [1, 2, 4, 5, 3]
# A single value required to remove from a list
print(f"After remove: {my_list}")

# pop([i]) - Removes and returns the element at position i in the list. If i is not specified, removes and returns the last element.
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Remove and return the third element (index 2)
removed_fruit = fruits.pop(2)
print(removed_fruit)  # Output: 'cherry'
print(f"After pop: {fruits}")  # Output: ['apple', 'banana', 'date', 'elderberry']

# Remove and return the last element
last_fruit = fruits.pop()
print(last_fruit)  # Output: 'elderberry'
print(f"After pop: {fruits}")  # Output: ['apple', 'banana', 'date']
# Requires a index number, otherwise it will pop the last element

# index(x[, start[, end]]) - Returns the index of the first occurrence of element x in the list. Optional arguments start and end specify the starting and ending positions for the search.