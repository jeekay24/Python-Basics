class Bird:
    def fly(self):
        print("Bird can fly")


class Airplane:
    def fly(self):
        print("Airplane can fly")


def lift_off(entity):
    entity.fly()


b = Bird()
a = Airplane()
lift_off(b)
lift_off(a)
