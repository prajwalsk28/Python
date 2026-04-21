print("--- Functions in Python ---")
# Function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. 
# It is used to perform a specific task and it helps in code reusability. It also makes the code more organized and easier to read.
# Syntax of a function in Python:
# def function_name(parameters):
#     # code to be executed i.e. some work to be done
#     return value )(optional - if you want to return a value from the function)
# function_name(arguments)

# Example of a function in Python:
def greet(name):    # This is the function definition. The function is named greet and it takes one parameter called name.
    print("Hello, " + name + ". Welcome to Python programming!")    # This is the body of the function. It prints a greeting message using the provided name. The + operator is used to concatenate the string "Hello, " with the value of name and the rest of the message.
greet("Alice")  # This is a function call. We are calling the greet function and passing the argument "Alice" to it. When this line is executed, the function will run and print the greeting message for Alice.
greet("Bob")        
# In the above example, we have defined a function named greet that takes one parameter name. The function prints a greeting message using the provided name. We then call the function twice with different arguments to see the output.
# Output: # Hello, Alice. Welcome to Python programming!
          # Hello, Bob. Welcome to Python programming!

# Example of a function with return value:
def add(a, b):    # This function takes two parameters a and b.
    return a + b   # It returns the sum of a and b. The return statement is used to exit the function and return a value to the caller. In this case, it returns the result of a + b.
result = add(5, 3)    # We call the add function with arguments 5 and 3, and store the returned value in the variable result.
print("The sum is:", result)    # This will print the result of the addition, which is 8.
# Output: The sum is: 8

def print_hello():
    print("Hello, World!")   # This function does not take any parameters and simply prints "Hello, World!" when called.
output = print_hello()    # We call the print_hello function and store its return value in the variable output. Since print_hello does not return anything, output will be None.
print("The return value of print_hello is:", output)    # This will print the return value of print_hello, which is None.
# Output: Hello, World!
# The return value of print_hello is: None

# Example of function to calculate average of 3 numbers:
def avg(a, b, c):
    return (a + b + c) / 3    # This function takes three parameters a, b, and c, and returns their average by summing them up and dividing by 3.
average = avg(10, 20, 30)    # We call the avg function with arguments 10, 20, and 30, and store the returned average in the variable average.
print("The average is:", average)    # This will print the calculated average, which is 20.0.
# Output: The average is: 20.0


print("--- Types of Functions ---")
# 1. Built-in Functions: These are functions that are provided by Python and are always available for use. Examples include print(), len(), type(), etc.
# In print() function, sep and end are optional parameters that allow you to customize the output. sep is used to specify the separator between multiple arguments, and end is used to specify what to print at the end of the output (default is a newline character).
# for example
print("Hello", "World", sep="-")    # This will print "Hello-World" because we have specified the separator as a hyphen.
print("Coding is", end=" ")    # This will print "Coding is" followed by a space instead of a newline, so the next print statement will continue on the same line.
print("FUN!")  # This will print "FUN!" on the same line as "Coding is" because we used end=" " in the previous print statement.
# Output: Hello-World
# Coding is FUN!

# 2. User-defined Functions: These are functions that you create yourself to perform specific tasks. You can define your own functions using the def keyword.

# 3. Lambda Functions: These are anonymous functions that are defined using the lambda keyword. They are typically used for short, simple functions that are not reused elsewhere in the code.

# 4. Recursive Functions: These are functions that call themselves in order to solve a problem. They typically have a base case to prevent infinite recursion.  


print("--- Function with default parameters ---")
# Example: 
def greet(name="Guest"):    # This function has a default parameter name with the value "Guest". If no argument is provided when calling the function, it will use the default value.
    print("Hello, " + name + ". Welcome to Python programming!")    
greet()    # We call the greet function without providing an argument, so it will use the default value "Guest".
greet("Alice")  # We call the greet function with the argument "Alice", which will override the default value and print a greeting for Alice.
# Output: Hello, Guest. Welcome to Python programming!  
        # Hello, Alice. Welcome to Python programming!

# Example
def prod(a, b=1):    # This function takes two parameters a and b, where b has a default value of 1. If b is not provided when calling the function, it will default to 1.
# NOTE: Always put parameters with default values at the end of the parameter list. If you put a parameter with a default value before a parameter without a default value, it will result in a syntax error.
# For example, def prod(a=1, b) would be incorrect and would raise a SyntaxError: non-default argument follows default argument.
    return a * b   # The function returns the product of a and b.
result1 = prod(5)    # We call the prod function with only one argument, 5. Since b has a default value of 1, it will calculate 5 * 1 and return 5.
result2 = prod(5, 3) # We call the prod function with two arguments, 5 and 3. This will calculate 5 * 3 and return 15.
print("The product is:", result1)    # This will print the product calculated with the default value of b, which is 5.
print("The product is:", result2)    # This will print the product calculated with the provided value of b, which is 15.
# Output: The product is: 5     
#         The product is: 15


print("--- Recursion ---")
# A recursive function is a function that calls itself in order to solve a problem. It typically has a base case to prevent infinite recursion.
# It is a powerful technique for solving problems that can be broken down into smaller, similar subproblems. 
# However, it is important to ensure that the base case is defined correctly to avoid infinite recursion and potential stack overflow errors.
# Call stack is a data structure that stores information about the active subroutines or functions in a program. When a function is called, a new frame is added to the call stack, which contains information about the function's parameters, local variables, and return address. When the function returns, its frame is removed from the call stack. In recursive functions, each recursive call adds a new frame to the call stack, and if the recursion goes too deep without reaching a base case, it can lead to a stack overflow error due to exceeding the maximum call stack size. 
# Example:
def show(n):
    if (n == 0):   # This is the base case for the recursion. If n is 0, the function will return and stop calling itself.
        return
    print(n)   # This will print the current value of n.
    show(n - 1)    # This is the recursive call. The function calls itself with n decremented by 1, which will continue until n reaches 0.
show(5)    # We call the show function with the argument 5. This will print the numbers 5, 4, 3, 2, and 1, and then stop when it reaches 0.
# Output: 5

# Example of a recursive function to calculate factorial:
def factorial(n):
    if (n == 0 or n == 1):    # This is the base case for the recursion. If n is 0 or 1, the function returns 1, since the factorial of 0 and 1 is defined as 1.
        return 1
    return n * factorial(n - 1)   # This is the recursive call. The function calls itself with n decremented by 1, and multiplies it by n to calculate the factorial.
    print(n)   # This line will never be executed because it is placed after the return statement. Once a return statement is executed, the function exits and any code after it will not run.
result = factorial(5)    # We call the factorial function with the argument 5. This will calculate 5! which is 5 * 4 * 3 * 2 * 1 = 120.
print("The factorial is:", result)    # This will print the calculated factorial, which is 120.
# Output: The factorial is: 120 
