def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello")

def inc(x):
    return x + 1
def dec(x):
    return x - 1
def operate(func, x):
    result = func(x)
    return result
print(operate)

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()
