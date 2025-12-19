import numpy as np
def input_matrix(matrix_num):
    print(f"Enter the value for matrix {matrix_num}")
    matrix = []
    for i in range(3):
        row = list(map(int,input(f"Enter row {i+1} : ").split()))
        matrix.append(row)
    return np.array(matrix)
matrix_1 = input_matrix(1)
matrix_2 = input_matrix(2)
result = np.dot(matrix_1,matrix_2)
print("matrix 1 :") 
print(matrix_1)
print("matrix 2 :")
print(matrix_2)
print("\n Matrix Multiplication : ")
print(result)
