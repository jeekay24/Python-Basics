from abc import ABC, abstractmethod


class MainFeatrue(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    def checkout(self):
        pass


class Employee():
    def login(self):
        print("i have logged in!")

    def logout(self):
        print("i have logged out!!")


e = Employee()
e.login()
e.logout()
