# Decorators.
## Extend or modify the behaviour of
## functions or without changing their code
## CALLBACKS<-->

#crown <--->
def my_deb(func):
    def wrapper():
        print("Calling hello world function")
        func()
        print("Finished calling hello world")
        for n in range(1,100):
            print("I Love Youu")

    return wrapper

@my_deb
def hello():
    print("hello world")

hello()

@my_deb
def greet():
    print("Greetings from above")

greet()