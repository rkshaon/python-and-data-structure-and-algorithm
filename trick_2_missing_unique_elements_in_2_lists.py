# You can be given 2 lists
# You may need to find the missing unique elements

list1 = ['a', 'b', 'b', 'c', 'd', 'd', 'e']
list2 = ['a', 'c', 'b']

print(set(list1) - set(list2))

# You can get missing elements in a list
print(list(set(list1) - set(list2)))