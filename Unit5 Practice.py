# WAP to print numbers from 1 to 100
i = 1
while i<=100:
    print(i)
    i = i + 1       # O/P : 1 2 3 4 5 6 7 8 9 10 .......100

# WAP to print numbers from 100 to 1
j = 100
while j>=1:
    print(j)
    j = j - 1       # O/P : 100 99 98 97 96 95 94 93 92 91 .......1

# WAP to print multiplication table of 7
i = 1
while i<=10:
    print("7 x",i,"=",7*i)
    i = i + 1       # O/P : 7 x 1 = 7 and so on till 7 x 10 = 70
# here we can also take user input for the number whose multiplication table is to be printed. Like n=7

# WAP to print squares of first 10 natural numbers
k = 1
while k<=10:
    print(k*k)
    k = k + 1       # O/P : 1 4 9 16 25 36 49 64 81 100

# WAP tp print the numbers in the given list
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0     # idx starts from zero because in python indexing starts from zero. So num[0] will give us the first element of the list which is 1.
while idx < len(num):
    print(num[idx])     #list_name[index] is the syntax to access the element at a particular index in a list.
    # here num[idx] will give us the element at index idx in the list num. So in the first iteration it will give us num[0] which is 1, in the second iteration it will give us num[1] which is 4 and so on till num[9] which is 100.
    idx = idx + 1

# WAP to search for a number x in the given tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
print(len(tup))   # O/P : 10 because there are 10 elements in the tuple
x = 36
idx = 0 #initialization
while idx < len(tup):
    if tup[idx] == x:
        print("number found at index",idx)
        break
    else:    
         print("number not found in the tuple") 
    idx = idx + 1

# WAP to search for the number x i given tuple using for loop
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0
for elem in tup:
    if (elem == x):
        print("number found at index",idx)
        break   # this will not check for the second occurrence of 49 which is at index 10. 
    # else:
    #     print("number not found in the tuple")
    idx = idx + 1

# WAP to give numbers from 100 to 1 using range function in for loop
for i in range(100, 0, -1):
    print(i)    

# Print multiplicaation table of number n using range
n = 6
for i in range(1,11):
    print(n*i)

# WAP to find sum of first n numbers using while and for loop
n = 10
i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1
print("sum of first",n,"numbers is",sum)

p = 5
sum = 0
for j in range(1, p+1):
    sum = sum + j   # here we are using p+1 because the stop value in range is exclusive. So if we want to include p in our range we have to use p+1 as the stop value.
    print("sum of first",p,"numbers is",sum)

# WAP to find factorial of first n natural numbers using while and for loop
n = 5
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i = i + 1
print("factorial of",n,"is",fact)

p = 5
fact = 1
for j in range(1, p+1):
    fact = fact * j 
print("factorial of",p,"is",fact)
