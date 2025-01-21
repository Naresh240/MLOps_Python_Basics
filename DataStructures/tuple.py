# Tuple is immutable data structure unlike list
# Tuple is also indexable data structure
# Tuple object is contains two functions: index, count

# Define empty tuple
tp = ()
print("Empty Tuple is: ", tp)

# Define tuple with some items
tp = (1, 2, 3, 4, 5, 6)
print("Tuple is: ", tp)

# Count function for tuple  --> It will print howmany times value 4 is there
tp = (1, 4, 2, 3, 4, 5, 4, 6)
tp_count = tp.count(4)
print("Count of 4 is: ", tp_count)

# Index function for tuple
tp = (1, 2, 3, 4, 5, 6)
tp_index = tp.index(2)
print("Index of 2 value is: ", tp_index)

# Print values with negative index
tp = (1, 2, 3, [4, 5], 6)
print("Values with negative indxes: ", tp[-2])

# Append function for tuple         --> With in tuple(list) we can append, not in tuple directly
tp = (1, 2, 3, [4, 5], 6)
tp[-2].append("Naresh")
print("Tuple after append: ", tp)