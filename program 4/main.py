# FUNCTIONS
# CREATING FUNCTIONS
def my_function() :
    print("This is my function!")

# FUNCTION CALLING
def print_data(data) :
    print(data)

print_data("Hello World!")

# WITH ARGUMENTS
def with_args(args) :
    print(args)

with_args("With Args!")

# WITH N NUMBER OF ARGS
def find_sum(*a) :
    print(a) # access args
    print(a[0]) # access by using index
    return sum(a)

print(find_sum(10, 20, 30))


# DECARATORS
def change_case(func) :
    def inner_func() :
        return func().upper()
    return inner_func

@change_case
def hello_world() :
    return "Hello World!"

print(hello_world())