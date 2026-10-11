# TWO DIMENTIONAL ARRAY AND MANIPULATION
import numpy as np

def display() -> int :
    print("#####################")
    print("1. Sort Array")
    print("2. Transpose of Array")
    print("3. Sum of rows")
    print("4. Sum of columns")
    print("5. Total Sum")
    print("6. Print Array")
    print("7. Exit")
    print("#####################")

    return int(input("Enter your choice : "))

limitx = int(input("Enter Limit X : "))
limity = int(input("Enter Limit Y : "))
array = np.zeros((limitx, limity), dtype=int)

for i in range(limity) :
    for j in range(limitx) :
        array[i, j] = int(input(f"Enter the value {i, j} : "))


while True:
    choice = display()

    if choice == 1 :
        print(np.sort(array))
    elif choice == 2 :
        print("Transpose of array :\n", array.T)
    elif choice == 3 :
        print(np.sum(array, axis=1))
    elif choice == 4 :
        print(np.sum(array, axis=0))
    elif choice == 5 :
        print(np.sum(array))
    elif choice == 6 : 
        print(array)
    else :
        break