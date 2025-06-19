delivery_partner = "swiggy"  # global-variable


def restaurant():
    order = "pizza"  # enclosed-variable

    def amount():
        quantity = 2  # local-variable
        print(
            f"I am going to order {quantity} {order} from {delivery_partner}")
    amount()


def greet():
    name = "ganesh"  # local-variable
    print(f"hello i am {name}")


greet()

restaurant()
print(f"Source : {delivery_partner}")
