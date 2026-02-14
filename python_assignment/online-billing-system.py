#Practice Problem 1: Online Shopping Billing System

#input
Customer = input("Enter your name : ")
Price = float(input("Enter product price : "))
Quantity = int(input("Enter the quantity : "))


#Couponcode
valid_coupons = ["SAVE20", "FESTIVE"]
CouponCode = input("You have a coupon code?(Y/N) : ")

if CouponCode == "Y":
    CouponCode1 = str(input("Enter Coupon Code : "))
else:
    pass

#PrimeMember
PrimeMember = input("Are you a Prime Member?(Yes/No) : ")


#generate bill

bill = 0

print("   ")
print(f'Customer : {Customer}')

bill = Price*Quantity

#discount
if Quantity > 5:
    discount = bill * 0.10
    bill -= discount
else:
    pass

#coupon code
if CouponCode1 in valid_coupons:
    bill -= 20
else:
    pass


#PrimeMember
if PrimeMember.lower() == "no":
    bill += 50
else:
    pass


print(f'Total before tax : {bill}')

#GST
GST = 0.18

total_gst_amount = bill * GST
final_amount = bill + total_gst_amount



#final response
print(f'GST : {total_gst_amount}')
print(f'Final Amount : {final_amount}')
print(f'Prime Member : {PrimeMember}')
print(f'Coupon Applied : {CouponCode1}')


#high value coustomer
if final_amount > 5000:
    print("High Value Coustomer")
else:
    pass





