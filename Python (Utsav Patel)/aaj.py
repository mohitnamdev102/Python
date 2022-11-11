def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def some():
    x = int(input("Please Enter Value 1: "))
    y = int(input("Please Enter Value 2: "))

    print("Addition is", add(x, y))
    print("Subtraction is", sub(x, y))
    print("Multiplication is", multi(x, y))
    print("Division is", div(x, y))


if __name__ == '__main__':
    some()
