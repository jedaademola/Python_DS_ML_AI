phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook)

phonebook1 = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
for name, number in phonebook1.items():
    print("Phone number of %s is %d" % (name, number))

del phonebook["John"]
print(phonebook)

phonebook.pop("Jack")
print(phonebook)
