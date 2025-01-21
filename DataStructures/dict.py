# Dict is enclosed by {} with key :value pair
# Dict can not store duplicate key
# Dict just like json dataset
# Dict keys are immutable where as Dict value can be immutable and mutable based on the nature of work
# Dict can be created using dict() and {} as well

# Define Dictionary
dct = {"empId": [101, 102, 103, 104], "empName": ["Naresh", "Suresh", "Anusha", "Srinu"], "empCity": ["Ongole", "Bangalore", "Hyderabad", "Chennai"]}
print("Dict is: ", dct)

# Print keys
print("Printing keys: ", dct.keys())
# Print values
print("Printing values: ", dct.values())
# Pritn items
print("Printing items: ", dct.items())

# Get function
# If some key we are trying to fetch without get function (e.g: dct(empId)) it will throw an exception, but if we go with get function it won't throw any exception 
dct = {"empId": 101, "empName": "Naresh", "empCity": "Ongole"}
print("Get empId by calling key without get function: ", dct["empId"])
print("Get empId by calling key without get function: ", dct.get("empId"))
print("Get empId by calling key without get function: ", dct.get("empAddress"))

# Pop function
dct = {"empId": 101, "empName": "Naresh", "empCity": "Ongole"}
print("Deleting city with empCity key: ", dct.pop('empCity'))
print("After deleting Dictionary is: ", dct)

## We can provide keys as int, string or tuple only
newDct = {1: 100, "A": "Naresh", (1,2): "Testing"}
print("Possible ways to provide Keys: ", newDct)

# Remove specific index from list which is existing under Dictionary
newDct = {"empId": [101, 102, 103, 104], "empName": ["Naresh", "Suresh", "Anusha", "Srinu"]}
print("Available employee names are: ", newDct['empName'])
newDct['empName'].remove('Srinu')
print("After applying remove employee: ", newDct['empName'])
newDct['empName'].pop(0)
print("After applying remove employee: ", newDct['empName'])

# Fromkeys function
# Using this function we can create dictionary very quickly, It will assign default as None
# With this we can assign same value to all keys
lst = [10, 20, 30, 40, 50]
print("Created Dictionay with none values: ", dict.fromkeys(lst))
print("Created Dictionay with none values: ", dict.fromkeys(lst, 'A'))

lst1 = [10, 20, 30, 40, 50, 20, 30, 40, 50]
update_list = list(dict.fromkeys(lst1).keys())
print("Write uniqube values of ", lst1, "is:", update_list)