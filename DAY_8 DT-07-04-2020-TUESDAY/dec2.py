def new_function(func):
    print("hello inside the fucntion")
    def wrapper_function():
        print("1st line ********")
        func()
        print("inside wrap")
    return wrapper_function

def new_decorator(var):
    print("the function indide the decoratoe is callled")
    def new_wrapper():
        print("the fucntioninside the wrapper is being called")
        var()
        print("after the function is being called after the printing alapha statement")
    return new_wrapper
# @new_function
# def hello():
#     print("hi")
#
#
# #hello()

@new_decorator
def new_func():
    print("alpha")

new_func()
