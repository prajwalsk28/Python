# WAP to store the following word meanings in a python dictionary.
# dog: "a small animal" ; period:"full stop","mensuration"
dict = {
    "dog": "a small animal",
    "period": ["full stop","mensuration"]
}
print(dict)


# One classroom is required for one subject form the given list of subjects. Calculate total number of classrooms required.
# "python", "java", "cpp", "python", "javascript", "c", "python", "cpp", "c", "java"
subjects = {"python", "java", "cpp", "python", "javascript", "c", "python", "cpp", "c", "java" }
print(subjects)
print("number of classrooms required:",len(subjects))


# WAP to enter marks of three subjects from user and store them in a dictionary. Start with an empty dictionary and add one by one. Store as subject:marks.
marks = {}
# x = int(input("Enter marks of Physics:"))
# marks.update({"Physics": x})

# x = int(input("Enter marks of Bio:"))
# marks.update({"Bio": x})

# x = int(input("Enter marks of Math:"))
# marks.update({"Math": x})

# print(marks)


# WAP to store 9 and 9.0 as seperate values in a set using built in data types.
# NOTE: hashing value of 9 and 9.0 is same in python i.e. both have with same value.
store = {9,"9.0"}
print(store)
# OR 
value = {
    ("float",9.0),
    ("integer",9)
}
print(value)