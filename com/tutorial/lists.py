mylist: list[int] = [1, 2, 3]

# mylist.append(1)
# mylist.append(2)
# mylist.append(3)

print(mylist[0])  # prints 1
print(mylist[1])  # prints 2
print(mylist[2])  # prints 3

print("Print Element using loop")
# prints out 1,2,3
for x in mylist:
    print(x)

# Lists can be joined with the addition operators:
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print("Print Element in Combined List")
print(all_numbers)
