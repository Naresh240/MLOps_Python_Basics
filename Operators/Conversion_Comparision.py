a1 = "1"
a2 = 1

print("Frist condtion check started...!!!!")
print("-----------------------------------")
if a1 == a2:
    print("a1 is a string and a2 is int, so both are not equal")
else:
    print("First condition failed")

print("  "*7)
print("  "*7)
print("Second condition check started...!!")
print("-----------------------------------")
if int(a1) == a2:
    print("a1 is a string but we converted into integer and comparing with a2")
    print("a1 and a2 are equal")
else:
    print("Second condition failed")

print("  "*7)
print("  "*7)
print("Third condition check started....!!")
print("-----------------------------------")
if a1 == str(a2):
    print("a1 is a string and a2 is integer but we converted into string then comparing with a1")
    print("a1 and a2 are equal")
else:
    print("Third condition failed")