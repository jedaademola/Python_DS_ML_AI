x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick1.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick2.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass
    print("statement is true")
elif another_statement is True:  # else if
    # do something else
    pass
    print("another_statement is true")
else:
    # do another thing
    pass
    print("do another thing")

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

print(not False)  # Prints out True
print((not False) == False)  # Prints out False
