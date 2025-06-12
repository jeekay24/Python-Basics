delivery_partner = "swiggy"


def restaurant():
    order = "pizza"

    def amount():
        quantity = 2
        print(
            f"I am going to order {quantity} {order} from {delivery_partner}")
    amount()


def greet():
    name = "ganesh"
    print(f"hello i am {name}")


greet()

restaurant()
print(f"Source : {delivery_partner}")
