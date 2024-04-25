#Importing NumPy library
import numpy as np
#Asking for input file
fname = input("Enter file: ")
#Make conditional statement about file name
if len(fname) < 1 : fname = "matrix1.txt"
#Make Matrix
i = np.loadtxt(fname, dtype='i', delimiter=',')
print("Matrix: ")
print(i)
print("Inverse Matrix: ")
#Make inverse Matrix
print(np.linalg.inv(i))