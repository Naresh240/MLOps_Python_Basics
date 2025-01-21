# List is a sequential data structure
# List is mutable
# List enclosed within the long bracket
# List can be create using [] and using list function
# List is indexable data structure in python

print("All functions from list: ", [i for i in dir(list) if "__" not in i])

# O/P: All functions from list:  ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# List creation
lst = []
lst1 = list()

print("Empty list: ", lst1)

# List with numbers
lst = [1, 2, 3, 4]
print("List with values: ", lst)

# List with strings
lst = ["India", "Srilanka", "America"]
print("List with strings: ", lst)

# List with different datatypes
lst = [1, 2, "India", "Srilanka", 3.45, True]
print("List with different datatypes: ", lst)

## 1. Append function --> we can append single item to at the end of the list
lst = [1, 2, 3, 4]
newList = ["India", "Srilanka", "America"]
lst.append(newList)
print("Final Appended list is: ", lst)

# O/P: Final Appended list is:  [1, 2, 3, 4, ['India', 'Srilanka', 'America']]

## 2. Extend function 
lst = [1, 2, 3, 4]
newList = ["India", "Srilanka", "America"]
lst.extend(newList)
print("Final Extended list is: ", lst)

# O/P: Final Extended list is:  [1, 2, 3, 4, 'India', 'Srilanka', 'America']

# Note: Only iterables can extend
# Iterable means just a container that can store some information
# e.g: string, list, tuples
# Numbers not iterable

# lst = [1, 2, 3, 4]
# lst.extend(5)
# print("Extendable list: ", lst)

# O/P: TypeError: 'int' object is not iterable

lst = [1, 2, 3, 4]
lst.extend("5")
print("Extendable list: ", lst)

## Append vs Extend
# Append we can use to append item at the end of the list as single index (it will increase lenth by 1 only)
# Extend can accept only iterables to extend a list, it will be increase length based on iterable length

## Length function for list 
lst = [1, 2, 3, 4]
list_lenght = len(lst)
print("Length of list is: ", list_lenght)

# Find 2 item index values
lst = [1, 2, 3, 4, 2, 5, 6, 7, 2]
Value_First_Time_index = lst.index(2)
print("Value_First_Time_index of list is: ", Value_First_Time_index)
Value_secound_Time_index = lst.index(2, lst.index(2, 1) + 1)
print("Value_First_Time_index of list is: ", Value_secound_Time_index)

# Insert function  --> using insert we can insert item based on index (syntax: list.insert(index, value))
lst = [1, 2, 3, 4]
lst.insert(2, "Naresh")
lst.insert(-1, "India")
print("Final insert value is: ", lst)

# O/P: Final insert value is:  [1, 2, 'Naresh', 3, 'India', 4]

# Insert one list in other list at specific index
lst1 = [1, 2, 3, 4]
lst2 = [5, 6]
lst1.insert(0, lst2)
print("List inserting in other list: ", lst1)

# If we want to insert value at the end of list
lst = [1, 2, 3, 4]
lst.insert(len(lst), "Naresh")
print("Using length function to find total length and adding new item: ", lst)

# Copy of List
lst = [1, 2, 3, 4]
lst1 = lst.copy()
print("Copy of lst list to lst1: ", lst1)

# Sorting of List   --> By defualt it will sort ascending order
lst = [5, 3, 6, 2, 4]
lst.sort()
print("Sorting of list is: ", lst)

# Sorting of list in descending order
lst = [5, 3, 6, 2, 4]
lst.sort(reverse=True)
print("Sorting in descending order: ", lst)

# Pop function in list
# Pop can popped item based on index, if we not passing any index in pop it will popped last item from list and it will return popped item
# If we use empty list it raise an exception
lst = [5, 3, 6, 2, 4]
lst.pop()
print("Popped item without  passing index is: ", lst)

# O/P: Popped item without  passing index is:  [5, 3, 6, 2]

lst.pop(1)
print("Remove index 1 value: ", lst)

# O/P: Remove index 1 value:  [5, 6, 2]

# Passing empty list
# lst = []
# lst.pop()
# print("Popping empty list: ", lst)

# O/P: IndexError: pop from empty list

## Remove function in list --> Remove item based on item's name
# Remove doesn't return anything like pop
lst = [5, 3, 6, 2, 4]
lst.remove(3)
print("After removing of 3 value: ", lst)
lst.remove(6)
print("After removing of 6 value: ", lst)
