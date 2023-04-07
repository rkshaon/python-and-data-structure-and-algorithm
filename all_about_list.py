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

# index(x[, start[, end]]) - returns the first occurrence of element in the list, optional arguments start and end specify the starting and ending positions for the search.
my_list = ['Cat', 'Dog', 'Elephant', 'Cat', 123, 'Cat', 1]
my_list.index('Cat') # 0
my_list.index('Elephant') # 2
# start optional arg
my_list.index('Cat', 1) # 3
# end optional arg
my_list.index('Cat', 4, 6) # 5
print(f"After search index of 'Cat': {my_list.index('Cat')}")
print(f"After search index of 'Elephant': {my_list.index('Elephant')}")
print(f"After search index of 'Cat' using start arg: {my_list.index('Cat', 1)}")
print(f"After search index of 'Cat' using end arg: {my_list.index('Cat', 4, 6)}")

# count(x) - Returns the number of occurrences of element x in the list.
fruits = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
fruits.count("cherry") # 2
print(f"After count: {fruits.count('cherry')}")

# sort(key=None, reverse=False) - Sorts the list in ascending order. Optional arguments key and reverse allow customization of the sorting behavior.
cars = ['Ford', 'BMW', 'Volvo', 'Mazda']
cars.sort() # ['BMW', 'Ford', 'Mazda', 'Volvo']
print(f"After sort: {cars}")
cars.sort(reverse=True) # ['Volvo', 'Mazda', 'Ford', 'BMW']
print(f"After sort reverse: {cars}")

# Here we want sort by the length of the item
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW', 'Volkswagen']
cars.sort(key=myFunc) # ['VW', 'BMW', 'Ford', 'Mitsubishi', 'Volkswagen]
print(f"After sort using key: {cars}")
cars.sort(key=myFunc, reverse=True) # ['Mitsubishi', 'Volkswagen', 'Ford', 'BMW', 'VW']
print(f"After sort using key and reverse: {cars}")

# Here we want to sort by year of the item
def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc) # [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]
print(f"After sort using key: {cars}")
cars.sort(key=myFunc, reverse=True) # [{'car': 'BMW', 'year': 2019}, {'car': 'VW', 'year': 2011}, {'car': 'Ford', 'year': 2005}, {'car': 'Mitsubishi', 'year': 2000}]
print(f"After sort using key and reverse: {cars}")

# reverse() - Reverses the order of elements in the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse() # ['cherry', 'banana', 'apple']
print(f"After reverse: {fruits}")

# copy() - Returns a shallow copy of the list
# The copy() method returns a copy of the specified list.
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy() # ['apple', 'banana', 'cherry', 'orange']
print(f"After copy: {fruits, x}")

# clear() - The clear() method removes all the elements from a list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear() # []
print(f"After clear: {fruits}")
