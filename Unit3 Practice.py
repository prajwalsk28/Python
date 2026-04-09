# WAP to take user input of 3 favorite movies and store them in a list.
# 1st method
movies = []
for i in range(3):
    movie = input("Enter your favorite movie: ")
    movies.append(movie)
print("Your favorite movies are: ", movies)

# 2nd method
movies = []
movies.append(input("Enter your 1st favorite movie: "))
movies.append(input("Enter your 2nd favorite movie: "))
movies.append(input("Enter your 3rd favorite movie: "))
print("Your favorite movies are: ", movies)


# WAP to check if a list contains a palindrome of elements. Use copy()
list_a = [1,2,3,2,1]
list_b = list_a.copy()  # This will create a copy of list_a and store it in list_b
list_b.reverse()       # This will reverse the order of items in list_b   
if(list_a == list_b):
    print("The list", list_a, "contains a palindrome of elements") 
else:
    print("The list", list_a, "does not contain a palindrome of elements")


# WAP to count the number of students with 'A' grade in following tuple.
grades = ('A', 'B', 'C', 'A', 'D', 'B', 'A')
print("No. of students with A grades:", grades.count('A'))  # This will count the number of occurances of 'A' in the tuple

# WAP to store the above tuple in a list and sort it in ascending order.
grades_list = list(grades)  # This will convert the tuple into a list
grades_list.sort()          # This will sort the items of the list in ascending order
print("Sorted list of grades:", grades_list)
