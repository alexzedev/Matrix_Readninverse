#Importuje bibliotekę NumPy
import numpy as np
#Pyta o nazwę pliku
fname = input("Enter file: ")
#Tworzy warunek dotyczący nazwy pliku 
if len(fname) < 1 : fname = "matrix1.txt"
#Tworzy Macierz
i = np.loadtxt(fname, dtype='i', delimiter=',')
print("Matrix: ")
print(i)
print("Inverse Matrix: ")
#Tworzy Macierz odwróconą
print(np.linalg.inv(i))