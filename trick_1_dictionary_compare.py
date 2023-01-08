# You can compare 2 dictionary
# that does they have same values
# They have to have same keys with same values
# They can have different order
# If keys and values are same
# Then they are same

dict1 = {
    'a': 3,
    'b': 10,
    'c': 19
}

dict2 = {
    'c': 19,
    'a': 3,
    'b': 10
}

dict3 = {
    'a': 3,
    'b': 10,
    'c': 10
}

print(dict1)
print(dict2)
print(dict3)
print(dict1 == dict2)
print(dict1 == dict3)
print(dict2 == dict3)