""" # Single Inheritance 
class dad:  # parent-class
    def house(self):
        print("yellow")


class child(dad):  # parent-class inherited into child-class
    def factory(self):
        print("red")

    def house(self):  # parent-class overwritten inside the child-class
        print("blue")


h = child()
h.house()
h.factory()
"""

""" # Multiple Inheritance
class dad:
    def house(self):
        print("white house")


class mom:
    def shop(self):
        print("flower shop")


class daughter(dad, mom):
    def factory(self):
        print("steel factory")


sp = daughter()
sp.factory()
sp.house()
sp.shop()
"""

"""  # Multi-level inheritance
class grandfather:
    def car(self):
        print("red car")


class dad(grandfather):
    def house(self):
        print("white house")


class son(dad):
    def factory(self):
        print("steel factory")


gk = son()
gk.car()
gk.factory()
gk.house()
"""

""" # Hierarchical inheritance
class dad:
    def house(self):
        print("white house")


class son1(dad):
    def market(self):
        print("fish market")


class son2(dad):
    def factory(self):
        print("steel factory")


r = son1()
g = son2()
r.house()
r.market()
g.house()
g.factory()
"""
