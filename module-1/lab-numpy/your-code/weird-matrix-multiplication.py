'''
Hello Codewarriors,

In this exercise you will have to multiply 2 numpy matrices (2d numpy arrays) in the following way:

Take each element of the first matrix and multiply by the second matrix
Place the resulting matrices in the same order as elements of the first matrix.
Important: use Numpy arrays as input and as output

If arrays with wrong shape (not 2d) or arrays with zero shape (shape=(0, 0)) are passed as an input, please return None

Examples:

I. A = [[2]]
B = [[1, 2], [3, 4]]
AB = [[2, 4], [6, 8]]

II. A = [[2, 3]]
B = [[40], [50]]
AB = [[80, 120], [100, 150]]

III. A = [[0, 1], [2, 3]]
B = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
AB = [[ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3]]
'''
import numpy as np

# A = np.array([2, 3])
# B = np.array([[40], [50]])
# AB = np.array([[80, 120], [100, 150]])
C = np.array([[0, 1], [2, 3]])
D = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
# CD = np.array([[ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 0, 0, 0, 1, 1, 1], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3], [ 2, 2, 2, 3, 3, 3]])
# dimension_AB = np.array(A.shape) * np.array(B.shape)
# # dimension_CD = np.array(C.shape) * np.array(D.shape)
# # print(A.shape, B.shape)
# # print(dimension_AB, AB.shape)
# # print(C.shape, D.shape)
# # print(dimension_CD, CD.shape)
# result = np.empty((dimension_AB[0],dimension_AB[1]))
# for i,b in enumerate(B):
#     for j,a in enumerate(A):
#         result[i,j] = a * b
# print(result)

def weird_matrix_mult(a, b):
    dimension_AB = np.array(a.shape) * np.array(b.shape)
    result = np.empty((dimension_AB[0],dimension_AB[1]))
    a_it = np.nditer(a, flags=['multi_index'])
    b_it = np.nditer(b, flags=['multi_index'])
    for x in a_it:
        for y in b_it:
            result[b_it.index, a_it.index] = x * y
    return result

print(weird_matrix_mult(C,D))