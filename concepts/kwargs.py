## *kwargs -> Key word arguments
## Dictionary{key:value}

def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)

greet(name="John",nationality="India")

#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)
    print("Name is",kwargs["name"])
    print("Age is",kwargs["age"])
    print("Degree is",kwargs["degree"])
    if "country" in kwargs:
        print("Country is",kwargs["country"])

    

#{key:value}
employee(name="Samson",age=20,degree="Engineering")
employee(name="John",country="Kenya",degree="Engineering",age=20)