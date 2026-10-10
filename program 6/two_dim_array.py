import numpy as np

# TWO DIMENSIONAL ARRAY
limitx = int(input("Enter Limit X : "))
limity = int(input("Enter Limit Y : "))
array = np.zeros((limitx, limity), dtype=int)

for i in range(limity) :
    for j in range(limitx) :
        array[i, j] = int(input(f"Enter the value {i, j} : "))

print(array)