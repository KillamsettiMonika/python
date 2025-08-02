#nested loop
# r=int(input("enter the no of rows: "))
# c=int(input("enter the no of columns: "))
# symbol=input("enter the symbol: ")
# for i in range(r):
#     for j in range(c):
#         print(symbol,end=" ")
#     print()
for i in range(1,10):
    while i%2==0:
        print(i, end=" ")
        i += 1
