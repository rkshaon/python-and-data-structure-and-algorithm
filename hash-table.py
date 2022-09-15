# Defination

# In computing, a hash table, also known as hash map, 
# is a data structure that implements an associative array 
# or dictionary. It is an abstract data type that maps 
# keys to values

# A hash table uses a hash function to compute an index, 
# also called a hash code, into an array of buckets or slots, 
# from which the desired value can be found. During lookup, 
# the key is hashed and the resulting hash indicates where 
# the corresponding value is stored.

# In Python, the Dictionary data types represent the implementation of hash tables.

# Visual Example
# https://d33wubrfki0l68.cloudfront.net/87075beeda9ac5cf3bc104aaca45d231ef42aaea/56f14/img/blog/data-structures/hash-tables/hash-table.png

# Example, Complexity, Usage, Implementation
# https://khalilstemmler.com/blogs/data-structures-algorithms/hash-tables/

# Resources
# https://youtu.be/APAbRkrqDVI
# https://realpython.com/python-hash-table/
# https://www.tutorialspoint.com/python_data_structure/python_hash_table.htm

# Creating dictionary
# Way 1
my_dict = {"Jessica": "001", "Alba": "002", "Scarlett": "003", "Johansson": "004"}
# Way 2
my_dict = dict(Jessica="001", Alba="002", Scarlett="003", Johansson="004")

# Nested dictionary
emp_details = {
    "Employee": {
        "Jessica": {
            "ID": "001",
            "Salary": "2000",
            "Designation": "Team Lead"
        },
        "Alba": {
            "ID": "002",
            "Salary": "1800",
            "Designation": "Associate Team Lead"
        },
        "Scarlett": {
            "ID": "003",
            "Salary": "1500",
            "Designation": "Senior Developer"
        },
        "Johansson": {
            "ID": "004",
            "Salary": "1200",
            "Designation": "Developer"
        }
    }
}

# Performing operations on Hash Table
# 1. Accessing Items
# 2. Updating Values
# 3. Deleting Entries

print(my_dict)
# Getting keys of the dictionary
print(my_dict.keys())
# Getting values of the dictionary
print(my_dict.values())
# Getting a specific key's value
print(my_dict.get("Alba"))
# Iterating all the keys present in the dictionary
# Way 1
for x in my_dict:
    print(x)
# Way 2
for x in my_dict.keys():
    print(x)
# Iterating all the values of the dictionary
for x in my_dict.values():
    print(x)
# Retrive all the key, value pairs of the dictionary
for x, y in my_dict.items():
    print(x, y)

# Dictionary is mutable data type
# Updating dictionary
my_dict["Alba"] = "005" # Exists, so value updated
my_dict["Shaon"] = "006" # Doesn't exist, so a new key, value pair added
print(my_dict)

# Deleting dictionary key, value pair
my_dict.pop("Johansson")
my_dict.popitem() # Delete the last item of the dictionary
del my_dict["Jessica"]

# Dataframe Defination

# Two-dimensional, size-mutable, potentially heterogeneous tabular data.

# Data structure also contains labeled axes (rows and columns). 
# Arithmetic operations align on both row and column labels. 
# Can be thought of as a dict-like container for Series objects. 
# The primary pandas data structure.

# References
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# Converting Dictionary into a Dataframe

import pandas as pd

data_frame = pd.DataFrame(emp_details["Employee"])
print(data_frame)

# print(my_dict)

# print(emp_details)

# print(type(my_dict))