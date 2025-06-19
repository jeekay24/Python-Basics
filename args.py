""" #args
def add(*args):
    total = 0
    for i in args:
        total += i

    return total


print(add(1, 2, 3, 4))
"""

""" #kwargs
def create_profile(**kwargs):
    print("Given user profile")
    for key, value in kwargs.items():
        print(f"{key}:{value}")


create_profile(name="ganesh", age=33, job="cloud engineer")
"""
