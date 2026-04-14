print("--- Loops in Python ---")
# Loops are used to execute a block of code repeatedly until a certain condition is met. There are two types of loops in Python: for loop and while loop.
print("--- While loop ---") 
# A while loop is used to execute a block of code as long as a specified condition is true. 
# The syntax of a while loop is:
# while condition:
      # code to be executed
# Example:
i = 1   # here i is called iterator
while i <= 5:
    print("hello world",i)
    i += 1  
print(i)    # 6 is printed because after the last iteration i becomes 6 and the loop condition becomes false.

j = 5
while j>= 1:
    print("welcome to python",j)
    j -= 1
print(j)    # 0 is printed because after the last iteration j becomes 0 and the loop condition becomes false.

print("--- Keywords in loop ---")
# 1] break: it is used to exit the loop when a certain condition is met.
# example:
i = 1
while i <= 10:
    print(i)
    if (i == 4):
        print("i is equal to 4, breaking the loop")
        break
    i += 1
print("loop exited")
# O/P : 1 2 3 4 because when i becomes 5 the loop will break and it will not print 5 and the loop will exit.

# 2] continue: it is used to skip the current iteration of the loop when a certain condition is met and continue with the next iteration.
# example:
j = 1
while j <= 10:
    if (j == 4):
        print("j is equal to 4, skipping the iteration")
        j += 1
        continue
    print(j)
    j += 1


print("--- For loop ---") 
# A for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
# The syntax of a for loop is:
# for variable in sequence:
    # code to be executed
# Example:
for i in range(1, 6):   # here i is called iterator and range is a built-in function that generates a sequence of numbers. The range(1, 6) generates a sequence of numbers from 1 to 5 because the stop value is exclusive.
    print("hello world",i)
# O/P : 1 2 3 4 5 because range(1,6) generates a sequence of numbers from 1 to 5.

list = [1, 2, 3, 4, 5]
for j in list:
    print("welcome to python",j)

tup = (1, 2, 3, 4, 5)
for k in tup:
    print("python is fun",k)

str = "bananaaaa"
for char in str:
    print(char)
print("loop is over")   # this else block will be executed after the loop is over.

# NOTE: we can also use break and continue keywords in for loop as we used in while loop. The syntax and usage is same as in while loop.
# Also the else block is used if we don't want to iterate after the break or continue statement.
# Example:
for i in range(1, 6):
    if (i == 4):
        print("i is equal to 4, breaking the loop")
        break
    print(i)
else:
    print("loop is over")   # this else block will not be executed because the loop is broken when i becomes 4.
 

print("--- Range ---") 
# The range() function is used to generate a sequence of numbers. It takes three parameters: start, stop and step. 
# The start parameter is the starting number of the sequence, the stop parameter is the ending number of the sequence and the step parameter is the increment value of the sequence. 
# The default value of start is 0 and the default value of step is 1. Thus both start and step are optional parameters. The stop parameter is a required parameter.
# SYNTAX: range(start?, stop, step?)
# Example:
for i in range(5):   # this will generate a sequence of numbers from 0 to 4 because the default value of start is 0 and the stop value is 5.
    print(i)    

for j in range(1, 6):   # this will generate a sequence of numbers from 1 to 5 because the start value is 1 and the stop value is 6.
    print(j)

for k in range(1, 10, 2):   # this will generate a sequence of numbers from 1 to 9 with an increment of 2 because the start value is 1, the stop value is 10 and the step value is 2.
    print(k)


print("--- Pass keyword ---") 
# The pass keyword is used as a placeholder for code that is not yet implemented. It is used when we want to create a function or a loop but we don't want to write the code for it yet.
# Example:
for i in range(1, 6):
    pass    # this will not do anything and the loop will run without any output. We can use this when we want to create a loop but we don't want to write the code for it yet.
print("some work")