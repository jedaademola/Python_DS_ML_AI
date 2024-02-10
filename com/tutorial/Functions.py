def sum_two_numbers(a, b):
    return a + b


# Define our 3 functions
def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s" % (username, greeting))


# print(a simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("Fareed Arogundade", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1, 2)
print("Sum of 2 number is %d " % x)

print("Exception Handling")


def do_stuff_with_number(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(5):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:  # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)


catch_this()

a = {"Jake", "Eric", "John", "Eric"}
print(a)
b = set(["John", "Jill"])
print(b)


