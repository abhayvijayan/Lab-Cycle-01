# DICTIONARIES
dict = {"name" : "Abhay", "department" : "Computer Science", "course" : "MSC", "main" : "Machine Learning"}
print(dict) # print dictionart
print(dict["name"]) # access elements by key

# TUPLES
num_tuple = (10, 20, 30, 40, 50)
print(num_tuple) # print tuple
print('Length Of Tuple : ', len(num_tuple)) # print length of tuple

fruits_tuple = ('apple', 'banana', 'cherry')
print(fruits_tuple)
print(fruits_tuple[0]) # print first element
print(fruits_tuple[1]) # print second element
print(fruits_tuple[2]) # print third element

# LISTS
fruits_list = ['apple', 'orange', 'banana']
print(fruits_list) # print list

fruits_list.append('cherry') # add element to the list
print(fruits_list)

fruits_list.remove('orange') # removing element from list
print(fruits_list)

print(fruits_list[0 : 3]) # access elemtns by using slicing

# SETS
set = {10, 20, 30, 40, 50}
set.add(60) # add element
set.remove(20) # remove element
print(set)