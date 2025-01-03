# WAP to ask the user to enter names of their 3 favorite movies and store them in a list
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy() method())
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("NOT palindrome")