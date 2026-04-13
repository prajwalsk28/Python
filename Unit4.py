print("---Dictionary---")
# Used to store data values in "key:value" pair
# They are unordered, mutable and don't allow duplicate keys
dict = {"name": "John", "age": 30, "marks": [85, 90, 92]}
print(dict)  

# Accessing values
print(dict["name"])  # Output: John

# Adding a new key-value pair
dict["city"] = "New York"
print(dict)  # Output: {'name': 'John', 'age': 30, 'marks': [85, 90, 92], 'city': 'New York'}

# Modifying an existing value
dict["age"] = 31
print(dict)  # Output: {'name': 'John', 'age': 31, 'marks': [85, 90, 92], 'city': 'New York'}

# We can create a null dictionary using dict() function
null_dict = {}
print(null_dict)  # Output: {}
null_dict["name"] = "Amit"
print(null_dict)  # Output: {'name': 'Amit'}

# Deleting a key-value pair
del dict["marks"]
print(dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}  

# Nested dictionary
nested_dict = {
    "name": "Surya Soldier",
    "bench": {
        "bicep": 16,
        "chest": 46,
        "shoulder": 18
    }
}
print(nested_dict)  # Output: {'name': 'Surya Soldier', 'bench': {'bicep': 16, 'chest': 46, 'shoulder': 18}}
print(nested_dict["bench"])
print(nested_dict["bench"]["shoulder"])  # Output: 18


print("---Dictionary Methods---")
# dict_name.get() - Returns the value of the specified key
print(dict.get("name"))  # Output: John
print(dict.get("country"))  # Output: None (since "country" key does not exist)
#NOTE: we access a non-existent key using dict_name[key], it will raise a KeyError
# print(dict["country"])  # This will raise a KeyError

# dict_name.keys() - Returns a list of all the keys in the dictionary
print(dict.keys())  # Output: dict_keys(['name', 'age', 'city'])

# dict_name.values() - Returns a list of all the values in the dictionary
print(dict.values())  # Output: dict_values(['John', 31, 'New York'])

# dict_name.items() - Returns a list of key-value pairs as tuples 
print(dict.items())  # Output: dict_items([('name', 'John'), ('age', 31), ('city', 'New York')])

# dict_name.update() - Updates the dictionary with new key-value pairs
dict.update({"country": "INDIA"})
print(dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'country': 'USA'}

# dict_name.pop() - Removes the specified key and returns its value
age = dict.pop("age")
print(age)  # Output: 31


print("---Set---")
# Used to store unordered collection of unique elements
# Each element in the set must be immutable (like numbers, strings, tuples) but the set itself is mutable
# We can't store mutable elements like lists or dictionaries in a set.

set1 = {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}
print(type(set1))
set2 = {2,3,4,4,"hii","byee","hii"}
print(set2)  
print(len(set2))    
# Output: {2, 3, 4, 'hii', 'byee'} 
#NOTE: duplicate elements are removed and order may vary

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
collection = {}   # This creates an empty dictionary, not a set


print("---Set Methods---")

# 1] Adding elements to a set
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}

# 2] Removing elements from a set
set1.remove(3)
print(set1)  # Output: {1, 2, 4, 5, 6}

# 3] To remove a random value from a set which is not empty
set1.pop()
print(set1) # Output: {2, 4, 5, 6}; 1 got popped and set was provided
print(set1.pop())   # Output: 2 was popped without set provided

# 4] To delete/empty an entire not empty set.
set3 = {"harry", "code", 0, 0, 7, 4}
set3.clear()
print(set3)     # Output: set()

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
# 5] To combine both set values and return a new set
print(set1.union(set2))     # Output: {1, 2, 3, 4, 5, 6}

# 6] To combine common values and returns a new set
print(set1.intersection(set2))  # Output: {3,4}