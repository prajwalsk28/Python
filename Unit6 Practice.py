# WAF to print length of a list where list is a parameter to the function.
cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
def list_length(list):  
    print(len(list))    # The function takes a list as a parameter and uses the built-in len() function to calculate and print the length of the list.
list_a = [1, 2, 3, 4, 5]
list_length(cities)    # This will print the length of the cities list, which is 5.
list_length(list_a)    # This will print the length of my_list, which is 5.
# Output: 5

# WAF to find the factorial of n where n is a parameter to the function.
def facto(n):   # The function takes an integer n as a parameter and initializes a variable facto to 1, which will be used to calculate the factorial.
    facto = 1    # The variable facto is initialized to 1 because the factorial of 0 is defined as 1, and it serves as the starting point for the multiplication in the loop. If n is 0, the loop will not execute and the function will return 1, which is correct for 0!.
    for i in range(1, n+1): 
        facto = facto * i    # The function uses a for loop to iterate from 1 to n (inclusive) and multiplies facto by each integer i in that range to calculate the factorial.
    print(facto)    # After the loop, it prints the calculated factorial of n.
facto(5)    # This will calculate and return the factorial of 5, which is 120.
# Output: 120

# WAF to print the elements of a list in a single line where list is a parameter to the function.
cities = ["Pune", "Mumbai", "Delhi", "Bangalore", "Chennai"]
def print_list(list):
    for item in list:   # The function takes a list as a parameter and uses a for loop to iterate through each item in the list.
        print(item, end=" ")    # It prints each item followed by a space (end=" ") to ensure that all items are printed on the same line.
print_list(cities)    # This will print the elements of the cities list on a single line.  
print()  # Add a newline between outputs
print_list(list_a)    # This will print the elements of list_a on a single line. 
print()
# Output: Pune Mumbai Delhi Bangalore Chennai

# WAP to convert USD in INR where USD is a parameter to the function. Assume 1 USD = 82 INR.
def converter(usd):    # The function takes an amount in USD as a parameter and converts it to INR using a fixed conversion rate.
    inr = usd * 82   # It multiplies the amount in USD by 82 to get the equivalent amount in INR.
    print(usd,"USD =", inr,"INR")   # It prints the converted amount in INR.
converter(10)    # This will convert 10 USD to INR and print the result, which is 820.
# Output: 10 USD = 820 INR


# Write a recursive function to calculate the sum of first n natural numbers where n is a parameter to the function.
def sum_natural(n):    # The function takes an integer n as a parameter and calculates the sum of the first n natural numbers using recursion.
    if (n == 0):
        return 0    # The base case is when n is 0, in which case the function returns 0, since the sum of the first 0 natural numbers is 0.
    return sum_natural(n-1) + n    # For n greater than 0, the function calls itself with n-1 and adds n to the result. This effectively sums up all numbers from 1 to n.
result = sum_natural(5)    # This will calculate the sum of the first 5 natural numbers, which is 1 + 2 + 3 + 4 + 5 = 15.
print("The sum of the first 5 natural numbers is:", result)    # This will print the calculated sum, which is 15.
# Output: The sum of the first 5 natural numbers is: 15 

# Write a recursive function to print all the elements in a list. Use index and list as parameters to the function.
def print_list(lst,idx):    # The function takes a list and an index as parameters and prints all the elements in the list using recursion. Can also write as def print_list(lst, idx=0) to set default value of idx to 0.
    if (idx == len(lst)):
        return    # The base case is when the index is equal to the length of the list, at which point the function returns and stops the recursion.
    print(lst[idx])   # It prints the current element at the given index.
    print_list(lst, idx + 1)   # It then calls itself with the next index to continue printing the rest of the list.

colors = ["Red", "Green", "Blue", "Yellow", "Purple"]
print_list(colors, 0)    # This will print all the elements in the colors list starting from index 0. It will print each color on a new line.