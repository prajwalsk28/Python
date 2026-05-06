print("--- File Input Output in Python ---")
# File handling is an important aspect of programming that allows you to read from and write to files. In Python, you can use the built-in open() function to work with files. 
# The open() function takes two parameters: the name of the file and the mode in which you want to open the file (e.g., 'r' for reading, 'w' for writing, 'a' for appending). 
# Python can be used to perform different operations on  a file (read and write data).
print("--- Types of files ---")
# 1. Text files- .txt, .docx, .log, .json etc
# 2. Binary files- .jpg, .png, .pdf, .exe etc
# At the end all the data is stored in binary format in the file, but we can read and write data in text format using text files. Binary files are used to store data in a format that is not human-readable, while text files are used to store data in a format that can be easily read and understood by humans.

print("--- File modes ---")
# 1. 'r' - Read mode: This is the default mode. It allows you to read the contents of a file. If the file does not exist, it will raise a FileNotFoundError.
# r+ - This mode allows you to read and write to a file. If the file does not exist, it will create a new file. If the file already exists, it will allow you to read and write to the file without overwriting the existing content.
# 2. 'w' - Write mode: This mode allows you to write data to a file. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file.
# w+ - This mode allows you to write and read to a file. If the file does not exist, it will create a new file. If the file already exists, it will allow you to write and read to the file without overwriting the existing content.
# 3. 'a' - Append mode: This mode allows you to add data to the end of a file without overwriting the existing content. If the file does not exist, it will create a new file.
# 4. 'x' - Exclusive creation mode: This mode allows you to create a new file. If the file already exists, it will raise a FileExistsError. 
# 5. 'b' - Binary mode: This mode is used to read or write binary files. It can be combined with other modes (e.g., 'rb' for reading a binary file, 'wb' for writing to a binary file).
# 6. 't' - Text mode: This is the default mode for text files. It can be combined with other modes (e.g., 'rt' for reading a text file, 'wt' for writing to a text file).
# 7. '+' - Update mode: This mode allows you to read and write to a file. It can be combined with other modes (e.g., 'r+' for reading and writing to a file, 'w+' for writing and reading to a file).         


print("--- File handling operations ---")
# 1. Opening a file: You can use the open() function to open a file. It returns a file object that you can use to perform various operations on the file.
# SYNTAX: file_object = open(file_name, mode)
# Example:
file = open("example.txt", "w")    # This will open a file named example.txt in write mode. If the file does not exist, it will create a new file. If the file already exists, it will overwrite the existing content.

# 2. Reading from a file: You can use the read() method to read the contents of a file. It returns the entire content of the file as a string.
file = open("example.txt", "r")    # This will open the file in read mode. If the file does not exist, it will raise a FileNotFoundError.
content = file.read()    # This will read the entire content of the file and store it in the variable content.
print(content)    # This will print the content of the file to the console.
# The read() method is used to read the contents of a file. It returns the entire content of the file as a string. If you want to read a specific number of characters, you can pass an argument to the read() method 
# e.g., file.read(10) will read the first 10 characters of the file. 
# You can also use the readline() method to read a single line from the file or the readlines() method to read all lines of the file into a list.

# 3. Writing to a file: You can use the write() method to write data to a file. It takes a string as an argument and writes it to the file.
file = open("example.txt", "w")    # This will open the file in write mode. If the file already exists, it will overwrite the existing content. If the file does not exist, it will create a new file.
file.write("This is a new line of text.\n")    # This will write the specified string to the file.
# The write() method is used to write data to a file. It takes a string as an argument and writes it to the file. .This will write the specified string to the file. 

# 4. Closing a file: After you are done working with a file, it is important to close it using the close() method. This will free up system resources and ensure that any changes made to the file are saved properly.
file.close()    # This will close the file. It is important to close the file after you are done working with it to free up system resources and ensure that any changes made to the file are saved properly.


# Program to demonstrate file handling in Python

# Open the file in read mode
file = open("example.txt", "r") 
# Read the contents of the file
content = file.read()
print(content)    # Print the content of the file to the console
# Use the readline() method to read a single line from the file
line1 = file.readline()
print(line1)    # Print the first line of the file to the console
# Use the readlines() method to read all lines of the file into a list
lines = file.readlines()    
print(lines)    # Print the list of lines to the console
# Close the file
file.close()  

# Open a file in write mode
file = open("example.txt", "a")    # This will open the file in append mode. If the file does not exist, it will create a new file. If the file already exists, it will add the new content to the end of the existing content.
# Write some data to the file
file.write("Hello, this is a file handling example in Python.\n")
file.write("This file is created for demonstration purposes.\n")   
# Close the file
file.close()        

# Open a file in over write mode
# This will open the file in write mode. If the file does not exist, it will create a new file. If the file already exists, it will overwrite the existing content.
# Example
file = open("example.txt", "r+")    # This will open the file in read and write mode. If the file does not exist, it will create a new file. If the file already exists, it will allow you to read and write to the file without overwriting the existing content.
file.write("This is an example of opening a file in read and write mode.\n")        
content = file.read()    # This will read the entire content of the file and store it in the variable content.
print(content)    # This will print the content of the file to the console.


# If there isnt a file named example.txt in the current directory, it will create a new file and write the specified content to it. If the file already exists, it will add the new content to the end of the existing content without overwriting it.
# Example 
file = open("sample.txt", "w")    # This will open a file named sample.txt in write mode. the file does not exist, it will create a new file. 
file.write("This is a sample file made completely new into existence.\n")    # This will write the specified string to the file.
file.close()    # This will close the file. It is important to close the file after you are done working with it to free up system resources and ensure that any changes made to the file are saved properly.


print("--- File handling using with statement ---")
# The with statement in Python is used to wrap the execution of a block of code within methods defined by a context manager. When working with files, using the with statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
# This is a more efficient and cleaner way to handle files compared to manually opening and closing them.
# Example of using with statement for file handling
with open("example.txt", "r") as file:    # This will open the file
    content = file.read()    # This will read the entire content of the file and store it in the variable content.
    print(content)    # This will print the content of the file to the console. 