# typecasting = The process of converting a value of one data type to another
#               (string, integer, float, boolean)
#               Explicit vs Implicit

name = "Bro"
age = 21
gpa = 1.9
student = True

# check what Datatype these variables are
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

# int > float
age = float(age)
print(type(age))

# float > int
gpa = int(gpa)
print(type(gpa))

# bool > str
student = str(student)
print(type(student))

# implicit casting
x = 2
y = 2.0

x = x / y
print(x)