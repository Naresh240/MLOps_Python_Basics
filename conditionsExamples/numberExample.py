number = input("Please provide number: ")

addition = int(number[0])+int(number[1])+int(number[2])

if addition == 6:
    print("Correct input..!!!")
else:
    print("Incorrect input...!!!")

## Other way
x = 123
y = str(x)

sum = int(y[0])+int(y[1])+int(y[2])
if sum == 6:
    print("Sum is correct")
else:
    print("Sum is incorrect")

## Otherway
z = 123

summation = int(str(x)[0])+int(str(x)[1])+int(str(x)[2])
if summation == 6:
    print("Summation is correct")
else:
    print("Summation is incorrect")
