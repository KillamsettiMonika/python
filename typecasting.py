#typecasting is a process of converting a variable from one data type to another, by using str(),int(),bool(),float()
name="monika"
age=21
gpa=9.16
is_student=True
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa=int(gpa)
print(gpa)
age=float(age)
print(age)

age=str(age)
age += "1"
print(age)
 
name=bool(name)
print(name)