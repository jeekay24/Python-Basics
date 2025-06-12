amt = int(input("Enter the paper bill amount: "))
if amt > 1000:
    disc = amt*0.1
    t_amt = amt-disc
else:
    t_amt = amt
gst = t_amt*0.18


def total():
    t = t_amt+gst
    print(f"The given amount is:{t}")


total()
