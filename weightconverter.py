weight=float(input("enter your weight "))
unit=input("kilograms or pounds (K/P) : ")
if unit == "K":
    weight = weight*2.205
    unit="pounds"
elif unit == "P":
    weight = weight/2.205
    unit="kilograms"
else:
    print("invalid unit")
print(f"your weight is {round(weight,2)} {unit}")