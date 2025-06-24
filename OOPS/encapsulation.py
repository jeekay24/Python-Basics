class Order:
    def __init__(self, cust_name, items, tot_amt, disc):
        self.cust_name = cust_name
        self.items = items
        self.__tot_amt = tot_amt
        self.__disc = disc

    def __calc_final(self):
        return self.__tot_amt - self.__disc

    def _get_admin_view(self):
        return {
            "Customer": self.cust_name,
            "Items": self.items,
            "Total amount": f"Rs.{self.__tot_amt}",
            "Discount applied": f"Rs.{self.__disc}",
            "Final bill": f"Rs.{self.__calc_final()}"
        }

    def get_cust_view(self):
        return {
            "Customer": self.cust_name,
            "Items": self.items,
            "Final bill": f"Rs.{self.__calc_final()}"
        }


class AdminPortal:
    def show_order(self, obj):
        return obj._get_admin_view()


class CustomerPortal:
    def show_order(self, obj):
        return obj.get_cust_view()


obj = Order("GK", ["chicken wings", "coke"], 700, 200)

admin = AdminPortal()
customer = CustomerPortal()

print("Admin View:")
print(admin.show_order(obj))

print("Customer View:")
print(customer.show_order(obj))
