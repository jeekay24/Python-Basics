# access specifiers for method
class Parent:
    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

    def access_from_same_class(self):
        self.public_method()
        self._protected_method()
        self.__private_method()


class Child(Parent):
    def access_from_child_class(self):
        self.public_method()
        self._protected_method()
        try:
            self.__private_method()
        except AttributeError:
            print("It is private;you cannot access it")


class Stranger():
    def access_from_another_class(self, obj):
        obj.public_method()
        obj._protected_method()
        try:
            obj.__private_method()
        except AttributeError:
            print("It is private;you cannot access it")


p = Parent()
print("\n Access from SAME class:")
p.access_from_same_class()
c = Child()
print("\n Access from SUB class:")
c.access_from_child_class()
st = Stranger()
print("\n Access from OTHER class:")
st.access_from_another_class(p)
