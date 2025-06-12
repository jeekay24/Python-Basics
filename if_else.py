print("\n Offer valid only for users with recharge scheme equal and above of Rs.399 and current data availability greater or equal to 1.5 GB")
print("----- Enter your details -----")
recharge_scheme = int(input("Enter your current scheme (in Rs):"))
curr_data = float(input("Enter your available data (in GB):"))

if recharge_scheme >= 399 and curr_data >= 1.50:
    print("eligible for 10% discount")
else:
    print("Either your scheme or curr data is not valid for the discount")
