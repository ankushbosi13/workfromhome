def decorator_func(function):
    def wrap():
        print("1st line in wrap")
        function()
        print("inside wrap 2nd function")
    return wrap

@decorator_func
def hello():
    print("funcalling")

#hello()

@decorator_func
def bye():
    print("see you late")


hello()
bye()


def new_function(param):
    print("1st line ********")
    def wrapper_function():
        param()
        print("inside wrap")
    return wrapper_function

@new_function
def hello():
    print("hi")


