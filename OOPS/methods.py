"""
# class-method

class Employee:

    company_name = "OPEN AI"

    @classmethod
    def company_name(cls, new_name):
        cls.company_name = new_name


Employee.company_name("Google")
print(Employee.company_name)


# static-method
class Math:
    @staticmethod
    def add(x, y):
        return x + y


print(Math.add(10, 20))
"""

"""
# diff between class and static method


class Employee:
    company_name = "OPEN-AI"

    @classmethod
    def change_company(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def try_change_company(new_name):
        company = new_name

#no object is created here since we can call call-method and static-method without any object creation itself
Employee.change_company("Google")
print("After classmethod:", Employee.company_name)

Employee.try_change_company("Meta")
print("After static method:", Employee.company_name)
"""
