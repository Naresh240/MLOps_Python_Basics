# Set data structure is an unorder collections of item
# Set doesn't allow duplicate item, means set will contain distinct items
# Set is a mutable datatype
# Set can created using set function
# Set can represented by {}
# Using set we can perform mathematical operations
# Set is a non-indexable data structure

st = {1, 3, 4, 5, 2}
print("Datatype of", st, "is:", type(st))


new_st = {1, 2, 4, 5, 2, 4}                     # Even if we provide duplicates also it will pick only distinct values
print("Datatype of", new_st, "is:", type(new_st))

# Add function in set
# If you want to add multiple items, it won't allow
st = {1, 3, 4, 5, 2}
st.add('Naresh')
print("After adding set is: ", st)

# Update function
st = {1, 3, 4, 5, 2}
st.update([1, 3, 4, 6, 3, 4, 5, 2])
print("After updating set is: ", st)

## Mathematicat Operations
# intersection, union, symmetric_difference, update etc.,
set1 = {1, 2, 4, 3, 6}
set2 = {4, 5, 2, 1}
print("Intersection value is: ", set1 & set2)
print("Union value is: ", set1 | set2)
# print("Union value is: ", set1.union(set2))
print("Symmetric difference is: ", set1 ^ set2)
# print("Symmetric difference is: ", set1.symmetric_difference(set2))
print("Difference of set1 from set2: ", set1.difference(set2))
print("Difference of set2 from set1: ", set2.difference(set1))

st1 = {1, 2, 5, 6}
st2 = {4, 2, 3}
print("Difference of set2 from set1: ", st2.isdisjoint(st1))

print("Difference update is:", st1 - st2)
# st1.difference_update(st2)
# print("Difference update is:", st1)

# Remove function in set
st1 = {1, 2, 5, 6}
st1.remove(6)
print("Remove item from set: ", st1)

# Discard function in set
st1 = {1, 2, 5, 6}
st1.discard(6)
print("Discard item from set: ", st1)

## Remove vs Discard
# Remove will raise exception if item is not exists in set, but discard will not raise any exception even if item not exists in set