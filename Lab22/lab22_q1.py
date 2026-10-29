def greet_decorator(func):
    def wrapper():
        print("Greetings!")
        func()
        print("...")
    return wrapper

@greet_decorator
def message():
    print("This is my first attempt at using decorator.")

message()