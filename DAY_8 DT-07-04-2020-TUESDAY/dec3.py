def decorator(func):
    def wrapper(x):
        print("1*********")
        func(x)
        print("2********")
    return wrapper


@decorator
def function_print_hello(greeting):
    print(greeting)

greeting = "hey"
function_print_hello(greeting)

