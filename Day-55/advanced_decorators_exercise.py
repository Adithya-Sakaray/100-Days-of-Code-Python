# Create the logging_decorator() function 👇

def func_description(function):
    def wrapper(*args):
        print(f"You called the function: {function.__name__}{args}")
        result = function(*args)
        print(f"It returned: {result}")

    return wrapper


# Use the decorator 👇

@func_description
def add(n1, n2):
    return n1 + n2


add(1, 2)