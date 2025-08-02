unit=input("is temp is in celsius or fahrenheit (C/F) : ")
temp=float(input("enter the temperature : "))
if unit == "C":
    temp=round((temp*9/5)+32,2)
    unit="fahrenheit"
elif unit == "F":
    temp=round((temp-32)*5/9,2)
    unit="celsius"
else:
    print("invalid unit")
print(f"the temperature is {temp} {unit}")