#length=float(input("lenth : "))
#width=float(input("width : "))
#area=length*width
#alt+0178 for cm² symbol
#print(f"area of rectangle is {area} cm²")
item = input("what item would you like to buy? ")
price = float(input("what is price of item? "))
quantity = int(input("how many do you want to buy? "))
total=price*quantity
print(f"you have bought {quantity} {item} and you have to pay {total} dollars as the price for one quantity is {price}")