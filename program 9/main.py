import numpy as np

# Random int
print("Random int : ", np.random.randint(1, 100))

# Random floating point
print("Random Float : ", np.random.rand())

# Random Array 1-D
arr1 = np.random.randint(1, 100, size=5)
print("Random 1-D Array : ", arr1)

# Random 2-D Array
arr2 = np.random.randint(1, 100, size=(3, 3))
print("Random 2-D Array : \n", arr2)

# Random float array
arr3 = np.random.random(size=5)
print("Random float array : ", arr3)