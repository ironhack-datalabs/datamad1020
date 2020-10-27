#1. Import the NUMPY package under the name np.
import numpy as np

#2. Print the NUMPY version and the configuration.

print(f"Numpy version: {np.__version__}")
print("-"*25)
print(np.show_config())
print('\n\n')

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.rand(2,3,5)
a = np.random.randn(2,3,5)
a = np.random.randint(0, 100, (2,3,5))

#4. Print a.

print(a)
print('\n\n')

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.

print(b)
print('\n\n')

#7. Do a and b have the same size? How do you prove that in Python code?

print(a.shape == b.shape)
print('\n\n')

#8. Are you able to add a and b? Why or why not?

"""
Cuando intentamos sumar el array 'a' al array 'b' nos aparece el siguiente error: Exception has occurred: **ValueError
operands could not be broadcast together with shapes (2,3,5) (5,2,3)**. Esto es debido a que la forma de ambos arrays no es la 
misma, pese a que su tamaño sí.
"""

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.transpose(1,2,0)

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c
"""
Porque ahora ambos arrays tienen el mismo tamaño y la misma forma: dos arrays de 3 filas y 5 columnas.
"""
#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print(a)
print('\n')
print(d)
print('\n\n')

"""
Como el array b se ha creado con la función 'ones()', esta devuelve los valores en formato float. Al sumarse con a, los valores
de este array pasan a ser floats también. 
"""

#12. Multiply a and c. Assign the result to e.

e = a*c

#13. Does e equal to a? Why or why not?

print(e == a)
print('\n\n')
"""
Ambas variables son iguales. Pese a que los números de e llegan en formato float, al no tener ningún valor después del punto, siguen siendo enteros.
"""

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(d_max, d_min, d_mean)
print('\n\n')

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np.empty((2,3,5))

"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""

condition_25 = (d > d_min) & (d < d_mean)
condition_75 = (d > d_mean) & (d < d_max)
condition_50 = d == d_mean
condition_0 = d == d_min
condition_100 = d == d_max

f[condition_0] = 0
f[condition_25] = 25
f[condition_50] = 50
f[condition_75] = 75
f[condition_100] = 100


"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print(d)
print('\n')
print(f)
print('\n\n')

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

condition_A = d == d_max
condition_B = (d > d_mean) & (d < d_max)
condition_C = d == d_mean
condition_D = (d > d_min) & (d < d_mean)
condition_E = d == d_min

"""
No sé si esta vale, la encontré en la la P**A BIBLIA (stackoverflow)
"""

f = f.astype('O')

f[condition_A] = 'A'
f[condition_B] = 'B'
f[condition_C] = 'C'
f[condition_D] = 'D'
f[condition_E] = 'E'

print(d)
print('\n')
print(f)
