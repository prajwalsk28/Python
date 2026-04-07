# WAP to take input name from user and print its length
name = input("Enter your name: ")
print("length of your name is: " ,len(name))

# WAp to find occurance of # symbol in the string
string = " #lol #fun #thisshitainral #hehe"
print("occurance of # symbol is: " ,string.count("#"))
 
 # WAP to check the number entered by the user is even or odd
num = int(input("Enter a number: "))
if(num%2==0):
    print(num,"is an even number")
else:
    print(num,"is an odd number")

# WAP to find the greatest of three numbers entered by the user
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
if(num1>num2 and num1>num3):
    print(num1,"is the greatest number")    
elif(num2>num1 and num2>num3):
    print(num2,"is the greatest number")
else:
    print(num3,"is the greatest number")

# WAP to check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))
if(num%7==0):
    print(num,"is a multiple of 7")
else:
    print(num,"is not a multiple of 7")
