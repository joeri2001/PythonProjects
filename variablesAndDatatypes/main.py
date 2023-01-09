# VARIABLE = a reusable container for storing a value
#            a variable behaves as if it were the value it contains

age = 21

# needs spaces manually inserted because it sees it as one big string.
print("You are " + str(age) + " years old.")

# doesn't need space because it's seperated by comma's, so the spaces are automatically added.
print("You are",age, "years old.")

# f before the string makes sure that you can print variables by inserting curly braces around them.
print(f"You are {age} years old.")


# DATATYPES

# INTEGER (whole numbers)
age = 21
players = 2

print(f"you are {age} years old")
print(f"there are {players} players online")

# FLOAT (number with comma)
hours = 6.20
euro = 5.50

print(f"{hours} hours have passed")
print(f"This product costs {euro} euro's")

# STRING (text)
name = "Joeri"
last_name = "Brinks"
email = "Testemail124@gmail.com"

print(f"Your first name is {name} and your last name is {last_name}.")
print(f"Your email is {email}")

# BOOLEAN (true or false)
online = True
for_sale = False
running = True

print(f"Are you online?: {online}")
print(f"Is the item for sale?: {for_sale}")

# usually used with if statements
if running:
    print("The game is running")
else:
    print("The game is not running")

# assign multiple variables to multiple values in one line
x, y, z = 1, 2, 3
print(x, y, z)
