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


p = Parent()
print("\n Access from SAME class:")
p.access_from_same_class()