print("---strings---")
# these are the data type that stores sequence of characters i.i alphabets
# strings can be enclosed in '',"" or ''' ''' 
str1 = "hello what's up!"
str2 = 'I am from India' 
str3 = '''nice to meet you bro'''
print(str1,str2,str3)

print("---Escape sequence characters---")
# characters used to modify the sequence of the statement after inserting a backslash \ 
# \n -> next line, \t -> 1 tab space between lines (blank spaces are also included)
str4 = "this is 1st sentence.\n this is the next one"
print(str4)

print("---Operations on string---")
# concatenation : joining strings
print(str1 + str2)
final = str1 + str3
space = str1 + "" + str3
print(final)
print(space)

# length : it is used to find the length of the string. "len" keyword is used
fruit = "mango"
len1 = len(fruit)
print(len1)
print(len(str2)) # spaces are also counted

print("---Indexing---")
# Each character in the string has a predefined position number called as index.
# Indexing in python starts from 0.
# It is used to access the characters from the given string.
string = "Random statement."
print(string[7])
print(string[6])    #Empty space is also shown.
# We can only access the character from the string and can't manipulate it by assigning some other character.

print("---Slicing---")
# It is used to access a part of a string.
# We must include the starting and the ending index.
# SYNTAX--- string_name[starting idx : ending idx] 
# Note : ending index is not included in the sliced string.
string = "Random statement."
print(string[5:7])
print(string[:11]) # this is same as [0:11] 
print(string[8:]) # this is same as [8:len(string)]

print("---Negative Slicing---")
# Like a number line, negative numbers are assigned to the string.
# The numbering starts from the end of string.
string = "Random statement."
print(string[-12:-5])

print("---String Function---")
# these are the reserve keywords in python used for carring out numerous functions
# SYNTAX--- string_name.function_name()

# 1} .endswith("") 
# This gives a boolean output for the characters provided in the ()
name = "Hi this is something"
print(name.endswith("lol"))
print(name.endswith("ing"))

# 2} .capitalize() 
# The 1st letter of the string is captalized.
# if we try to print the string again, it'll provide the original string
gadget = "anywhere door"
print(gadget.capitalize())
print(gadget) # returns original string

# 3} .replace("old","new")
# Used to replace the old character or word of the string with the new one. 
example = "i don't know what to say lol"
print(example.replace("o","q"))
print(example.replace("lol","hehe"))

# 4} .find()
# Used to give the index of the 1st occurance of the provided character in the string.
string = "Random statement."
print(string.find("e"))
print(string.find("q")) # returns -1 if character not available.

# 5} .count()
# Returns the number of occurances of a character or substring in a string
stmt = " lol idk lol what is this lol lol"
print(stmt.count("lol"))
print(stmt.count("i"))

print("---Conditional Statements---")
# 1] if-elif-else staatement:
# Syntax:- if(condition):
#             statement 1
#          elif(condition):
#             statement 2
#          else:
#             statement n
# Example:
age = int(input("Enter your age: "))
if(age>=18):
    print("Can drive")
    print("Can vote")
elif(age==18):
    print("Just became an adult")
else:
    print("Cannot drive")
    print("Cannot vote")
    print("is a kiddo")
