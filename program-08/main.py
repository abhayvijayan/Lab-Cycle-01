import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A :\n", A)
print("Matrix B :\n", B)


# ADDITION
print("Addition : \n", A + B)

# SUBTRACTION
print("Subtraction : \n", A - B)

# MULTIPLICATION
print("Matrix Multiplication : \n", A @ B) # @ operator is used to multiplay rows against columns :)

print("Element  Wise Multiplication : \n", A * B)

# TRANSPOSE
print("Transpose Of A : \n", A.T)

# DETERMINANT
print("Determinant of B : ", np.linalg.det(A))

# INVERSE
print("inverse Of A : \n", np.linalg.inv(A))