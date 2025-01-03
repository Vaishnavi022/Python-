# Append method (Mutating list add the another number)
list = [5,2,3,4]
list.append(4)
print(list)

# Sort in ascending order
print(list.sort()) 

#sort in descending order
list1 = ["Apple","Banana","Litchi","Strawberry"]
print(list1.sort(reverse=True))
print(list1)

#Insert method
list2 = [2,1,3]
list2.insert(1,5)
print(list2)

#Remove method (remove the element)
list2.remove(1)
print(list2)

#Pop method (remove the particular index element)
list2.pop(2)
print(list2)
