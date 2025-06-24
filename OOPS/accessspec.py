# access specifiers for variables

"""#other form of this class
class Parent:
    def __init__(self, pub, priv, prot):
        self.pub_var = pub
        self._priv_var = priv
        self.__prot_var = prot

    def access_from_same_class(self):
        print("Inside the parent class")
        print("Public:", self.pub_var)
        print("Private:", self._priv_var)
        print("Protected", self.__prot_var)


a = Parent("I am public", "I am private", "I am protected")
a.access_from_same_class()
"""


class Parent:
    def __init__(self):
        self.pub_var = "I am public"
        self.__priv_var = "I am private"
        self._prot_var = "I am protected"

    def access_from_same_class(self):
        print("Inside the parent class:")
        print("Public:", self.pub_var)
        print("Private:", self.__priv_var)
        print("Protected:", self._prot_var)


class Child(Parent):
    def access_from_sub_class(self):
        print("Outside parent class:")
        print("Public:", self.pub_var)
        # not recommended since its name-mangling
        print("Protected:", self._prot_var)
        try:
            print("Private:", self.__priv_var)
        except AttributeError:
            print("It is private: you cannot access it")


class Stranger():
    def access_from_some_other_class(self, obj):
        print("In other class:")
        print("Public:", obj.pub_var)
        # not recommended since its name-mangling
        print("Protected:", obj._prot_var)
        try:
            print("Private:", obj.__priv_var)
        except AttributeError:
            print("It is private: you cannot access it")


a = Parent()
print("\n Access from SAME class:")
a.access_from_same_class()
s = Child()
print("\n Access from SUB class:")
s.access_from_sub_class()
st = Stranger()
print("\n Access from OTHER class:")
st.access_from_some_other_class(a)
