# What is Set?
# In Python, a set is an unordered collection of unique elements. 
# It is defined using curly braces {} or the set() constructor. 
# Sets are mutable, meaning you can add, remove, and modify their 
# elements. 

# Example
# my_set = {1, 2, 3}

# create set
my_set = {1, 2, 3}  # Using curly braces
print(my_set) # {1, 2, 3}
my_set = set([1, 2, 3])  # Using the set() constructor
print(my_set) # {1, 2, 3}

# access set
for element in my_set:
    print(element) # 1 \n 2 \n 3

if 1 in my_set:
    print("1 is in the set") # 1 is in the set

# modify set
# add
my_set.add(4)  # Add a single element
print(my_set) # {1, 2, 3, 4}
my_set.update([5, 6])  # Add multiple elements from an iterable
print(my_set) # {1, 2, 3, 4, 5, 6}


# remove
my_set.remove(3)  # Remove an element by value (raises KeyError if not found)
print(my_set) # {1, 2, 4, 5, 6}
my_set.discard(2)  # Remove an element by value (does nothing if not found)
print(my_set) # {1, 4, 5, 6}
popped_element = my_set.pop()  # Remove and return an arbitrary element from the set
print(my_set) # {4, 5, 6}
print(popped_element) # 1
my_set.clear()  # Remove all elements from the set
print(my_set) # set()

# set operations
# union
set1 = {1, 3, 5}
set2 = {2, 4, 6}
union_set = set1 | set2 # union operation
print(union_set) # {1, 2, 3, 4, 5, 6}
union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 4, 5, 6}

# intersection
set1 = {1, 2, 3, 5}
set2 = {2, 4, 6}
intersection_set = set1 & set2  # intersection operation
print(intersection_set) # {2}
intersection_set = set1.intersection(set2)
print(intersection_set) # {2}

# diffrence
set1 = {1, 2, 3, 5}
set2 = {2, 4, 5, 6}
difference_set = set1 - set2 # difference operation
print(difference_set) # {1, 3}
difference_set = set1.difference(set2)
print(difference_set) # {1, 3}

# symmetric difference
set1 = {1, 2, 3, 5}
set2 = {2, 4, 5, 6}
symmetric_diff_set = set1 ^ set2
print(symmetric_diff_set) # {1, 3, 4, 6}
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set) # {1, 3, 4, 6}

# Set comprehension
my_set = {x for x in range(1, 5)}
print(my_set) # {1, 2, 3, 4}

# Set methods
# len(): Returns the number of elements in the set.
print(len(my_set)) # 4

# copy(): Returns a shallow copy of the set.
my_set2 = my_set.copy()
print(my_set2) # {1, 2, 3, 4}

# isdisjoint(other_set): Returns True if the set has no common elements with other_set.
set1 = {1, 3, 5}
set2 = {2, 4, 6}
print(set1.isdisjoint(set2)) # True

set1 = {1, 2, 3, 5}
set2 = {2, 4, 6}
print(set1.isdisjoint(set2)) # False

# issubset(other_set): Returns True if every element in the set is also in other_set.
set1 = {2, 6}
set2 = {1, 2, 3, 4, 5, 6}
print(set1.issubset(set2)) # True

# issuperset(other_set): Returns True if every element in other_set is also in the set.
set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 6}
print(set1.issuperset(set2)) # True