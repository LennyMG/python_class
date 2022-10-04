#ASSIGN A VALUE OF "Apple" INTO A KEY "FRUIT"
FRUIT = "apple"

#Show the value of the FRUIT key
print(FRUIT)


#SHOWS THE LOCATION OF THE STRING
print(id(FRUIT))

#SHOWS THE DATA TYPE 
print(type(FRUIT))

# #Shoes the methods of the string
# print(dir(FRUIT))

#capitalize the first letter
print(FRUIT.capitalize())


#Find how many times p is repeated
print(FRUIT.count("p"))


#Find out if the string starts with somtehing
print(FRUIT.startswith("app"))

#Find out if the string ends with something
print(FRUIT.endswith("pple"))

# Change to uppercases
print(FRUIT.upper())


# Create new vaiable
INCORRECT_STRING = "    space_string    "

#Remove spaces on the left side
print(INCORRECT_STRING.lstrip())

#Remove spaces on the right side
print(INCORRECT_STRING.rstrip())

#Remove spaces on both side
print(INCORRECT_STRING.strip())










