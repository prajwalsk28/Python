print("Let's begin!")

# print -> function
# character set in python = A-Z, a-z, 0-9, sp. symbols(!,@,#,$)
# anything inside ("") is called input, which is shown in the terminal as an output.

print("This is statement 1", "and this is second one on same line")
print(67)           # no "" required for digits. Only for strings
print(25+54)            # any operator

# Variable is a block of memory in which value is stored. (value can be string, integer, float)
# Variable - assignment operator - value to be stored in variable
# multi line comment -> select texts and ctrl + / 
name = "Rohan"
age = 19
height = 5.46
print(name)
print("my name is",name)
print("my age is",age)
print("I am",height,"feet tall")
length = height         # reassigning the variable
print(length)           

print("---Rules for names of variables---")
# variables are a.k.a identifiers
# 1] Valid combination of upper and lower case letters, digits and underscores.
# 2] Cannot start with digit i.e. 1variable is not valid.
# 3] Cannot use special symbols in identifiers.
# 4] Any length of identifier is valid.

print("---Data Types---")
# type of data stored in variable.
# there are 5 primary data types

# 1] Integer : Used to store +ve , -ve and 0 numbers
num = -28
print(num)
print(type(num))        

# 2] String : used to store characters A-Z , a-z in ""
naam = "shabana"
print(naam)
print(type(naam))

# 3] Float : stores values consisting digits after decimal
pi = 3.1425799846845
print(pi)
print(type(pi))

# 4] Boolean : returns True or False statement . 1st letter always capital.
tall = False
print(type(tall))

# 5] None : No value is stored in this data type
a = None 
print(type(a))

#---Keywords---
# reserve words in python having fixed meaning
# are case sensitive
# cannot be used as variables
# e.g and, break, class, def, else, False, if, None, lambda, True, return 

print("---Operators---")
# operator is a symbol performing operation between operands.

# 1] Arithmetic: +,-,*,/,%,**
x = 25 
y = 4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)  # returns remainder
print(x**y) # x^y
print("------")

# 2] Relational/comparision: returns answer in T or F
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print("------")

# 3] Assignment: used to assign value to a given variable
n = 24
n = n + 12
print(n)
n += 12
print(n)
n -= 12
print(n)
n *= 12
print(n)
n /= 12
print(n)
n **= 4     # power
print(n)
n %= 5      # remainder
print(n)
print("------")

# 4] Logical : and  , or and not operator used to provide logical answer true or false.
val1 = False
val2 = False
print("Logical and operator:", val1 and val2) # here False cuz T&T=T, T&F=F
print("Logical or operator:", val1 or val2)
print("Logical or operator:",(val1 ==val2) or val2)

A = 22
B = 6
print("Logical not operator:", not(A>B))
print("------")

print("---Type casting conversion---")
# we convert appropriate data type from int to float and string to bool and vice versa
# but if we try to convert a string into integer then it will be not possible as we cannot perform mathemtical operations on it
# also if we perform mathematical operation on int and float value then it will provide result as an float value
# this is because float value can store extra information inside it compared to int value
e = 24
# e = "21" is invalid as it can only concatenate str (not "float") to str
f = 6.123
f_ = "6.123"
print(type(f_))
print(e+f)
here = float(25)
print(type(here))
print("------")

print("---Input statements---")
# These are used to accept values from user
lol = input("Enter your name: ")
print("my name is WHAT my name is WHO name is chik chik",lol) 
# we can also get to kow the data type on input value
print(type(lol))
value = input("enter something random: ")
print(type(value),value)      # the input value will be considered as string no matter whatever you enter 
# above variable value will give string as an output
# to get output as an integer use int datatype before using input statement
value1 = int(input("enter some shit: "))
print(type(value1),value1)     # this will only take input as a integer  and any other data type will be invalid
urname = input("enter your name: ")
urage = int(input("enter your age: "))
marks = float(input("enter your marks: "))
print(type(urname),urname)
print(type(urage),urage)
print(type(marks),marks)