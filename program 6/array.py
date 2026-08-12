import numpy as np

array = []

# ONE DIMENSIONAL ARRAY
limit = int(input("Enter limit : "))
for i in range(limit) :
    array.append(int(input("Enter element : ")))


my_array = np.array(array)
print(my_array)

# TWO DIMENSIONAL ARRAY
