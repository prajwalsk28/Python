print("---Lists---")
# Lists are used to store elements of different types (int,float,str etc.) in a single variable.
# Lists are created using square brackets [] and items are separated by commas.
# SYNTAX--- list_name = [item1, item2, item3, ...]

marks = [90, 85, 78, 92, 88]
print(marks)
print(type(marks))
print(len(marks))   # gives the number of items in the list
print(marks[0])    # gives the 1st item of the list (index starts from 0)

# We can also create a list with different types of data.
my_list = [1, 3.14, "Hello", True]
print(my_list)
print(type(my_list))

# In strings we can only access the characters but in lists we can access and manipulate the items by assigning some other value to it.
str = "Hello"
#str[0] = "y"   # This will give an error because strings are immutable (can't be changed)

my_list[0] = 10   # This will change the 1st item of the list to 10 because lists are mutable (can be changed)
print(my_list)
# we can only access the values within the range of the list. If we try to access an index that is out of range, it will give an error.
# print(my_list[8])  # This will give an error because there is no item


print("---Slicing in Lists---")
# Slicing in lists is similar to slicing in strings. We can access a part of the list by providing the starting and ending index.
# SYNTAX--- list_name[starting idx : ending idx]
# note that ending index is not included in the sliced list.
marks = [90, 85, 78, 92, 88]
#       0   1   2   3   4
#      -5  -4  -3  -2  -1
print(marks[1:3])  # This will give the items from index 1 to 2 (ending index is not included)
print(marks[:4])   # This is same as [0:4]
print(marks[-5:-3])  # This will give the items from index -5 to -4 (ending index is not included)


print("---List Functions/Methods---")
# These are the reserve keywords in python used for carrying out numerous functions on lists.
list1 = [6, 7, 9, 3, 4, 1, 5]
print(list1)

# 1} .append(item)
# This is used to add an item at the end of the list.
list1.append(6)
print(list1)

# 2} .insert(index, item)
# This is used to add an item at the specified index in the list.
# SYNTAX--- list_name.insert(index, item)
list1.insert(2, 10)  # This will add 10 at index 2
print(list1)

# 3} .sort()        in ascending order
# This is used to sort the items of the list in ascending order.    
list1.sort()
print(list1)

# 4} .sort(reverse=True)     in descending order
# This is used to sort the items of the list in descending order.
list1.sort(reverse=True)
print(list1)

# 5} .reverse()
# This is used to reverse the order of the items in the list.
list1.reverse()
print(list1)

# 6} .remove(item)
# This is used to remove the first occurrence of the specified item from the list.
list1.remove(6)  # This will remove the first occurrence of 6 from the list
print(list1)

# 7} .pop(index)
# This is used to remove the item at the specified index from the list and returns it.
# If index is not provided, it removes and returns the last item of the list.   
removed_item = list1.pop(3)  # This will remove the item at index 3 and return it
print(list1)
print("Removed item:", removed_item)

list1.pop()  # This will remove and return the last item of the list
print(list1)

# 8} .index(item)
# This is used to return the index of the first occurrence of the specified item in the list.
index_of_9 = list1.index(9)  # This will return the index of the first occurrence of 9 in the list
print("Index of 9:", index_of_9)

# NOTE: All above functions/methods modify the original list and do not return a new list. If we try to print the result of these functions, it will return None because they do not return any value.
print(list1.append(11))  # This will add 11 at the end of the list but will return None
print(list1)

# NOTE: for lists like ("apple", "banana", "kiwi", "mango") all functions/methods will work on the basis of alphabetical order. 
# #For example, if we try to sort this list, it will be sorted in alphabetical order (apple, banana, kiwi, mango) and not in the order of their length or any other criteria.


print("---Tuples---")
# Tuples are used to store elements of different types (int, float, str etc.) in a single variable.
# Tuples are created using parentheses () and items are separated by commas.
# Unlike lists, tuples are immutable (can't be changed) and do not have any built-in functions/methods to modify them.
# SYNTAX--- tuple_name = (item1, item2, item3, ...)
marks = (90, 85, 78, 92, 88)
print(marks)
print(type(marks))
print(len(marks))   # gives the number of items in the tuple
print(marks[0])    # gives the 1st item of the tuple (index starts from 0)
# marks[0] = 95   # This will give an error because tuples are immutable (can't be changed)

tup = (1)   # This is not a tuple, it is just an integer. 
print(type(tup))  # This will print <class 'int'>
#To create a tuple with a single item, we need to add a comma after the item.
tup = (1,)  # This is a tuple with a single item
print(type(tup))  # This will print <class 'tuple'>


print("---Slicing in Tuples---")
# Slicing in tuples is similar to slicing in lists and strings. We can access a part of the tuple by providing the starting and ending index.
# SYNTAX--- tuple_name[starting idx : ending idx]
marks = (90, 85, 78, 92, 88)
print(marks[1:3])  # This will give the items from index 1 to 2 (ending index is not included)
print(marks[:4])   # This is same as [0:4]
print(marks[-5:-3])  # This will give the items from index -5 to -4 (ending index is not included)


print("---Tuple Functions/Methods---")
# These are the reserve keywords in python used for carrying out numerous functions on tuples.
tuple = ("lion", "tiger", "leopard", "cheetah", "panther")

# 1} .count(item)
# This is used to count the number of occurrences of the specified item in the tuple.       
print(tuple.count("lion"))  # This will count the number of occurrences of "lion" in the tuple

# 2} .index(item)
# This is used to return the index of the first occurrence of the specified item in the tuple.
print(tuple.index("leopard"))  # This will return the index of the first occurrence of "leopard" in the tuple
