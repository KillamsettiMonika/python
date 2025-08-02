# name=input("enter your name :")
# if name =='':
#     print("name is empty")
# else:
#     print(f"hello {name}")

# while name == '':
#     print("nam eis empty")
#     name=input("enter your name :")
# print(f"hello {name}")

# age= int(input("enter your age :"))
# while age <0:
#     print("age is invalid")
#     age = int(input("enter your age :"))
# print(f"your age is {age}")

# food = input("enter your favorite food (q to quit):")
# while not food=='q':
#     print(f"your favorite food is {food}")
#     food = input("enter your favorite food (q to quit):")
# print("bye")

num=int(input("enter a number 1-10 :"))
while num <1 or  num>10:
    print("number is invalid")
    num = int(input("enter a number 1-10 :"))
print(f"your number is {num}")