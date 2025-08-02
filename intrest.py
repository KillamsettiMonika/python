#compound interest calculator
p=0
r=0
t=0
while True:
    p = float(input("Enter principal amount (positive number): "))
    if p<0:
        print("Principal amount must be a positive number.")
    else:
        break
while True:
    r = float(input("Enter rate (positive number): "))
    if r<0:
        print("rate must be a positive number.")
    else:
        break
while True:
    t = float(input("Enter time (positive number): "))
    if t<0:
        print("time must be a positive number.")
    else:
        break
total=p*pow((1+r/100),t)
print(f"Total amount after {t} years is: {total:.2f}")
