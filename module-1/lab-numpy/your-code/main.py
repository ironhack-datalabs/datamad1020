#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.

"""
print(np.version.version)
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

import random


a = np.random.random((2,3,5))
"""
a1 = np.random.randint((2,3,5))

#a2 = np.array([[1,2],[3,4],[5,6]])

#a2.reshape((2,3,5))"""

#4. Print a.

"""
print(a)

print(a1)


##print(a2)
"""
#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"


b = np.ones((5,2,3))



""""""

#6. Print b.

"""
print(b)
"""

#7. Do a and b have the same size? How do you prove that in Python code?

"""
print(a.size)

print(b.size)

print((a.size) == (b.size))

Con el comando size sale que los dos tienen el mismo tamaño
"""

#8. Are you able to add a and b? Why or why not?

""" 
c = a + b
print(c)

print(a.shape)

print(b.shape)


Al hacer la operación sale el siguiente error: 'operands could not be broadcast together with shapes (2,3,5) (5,2,3)'
Eso significa que como no tiene la misma medida no se puede en este caso sumar (a tiene (2,3,5) y b tiene (5,2,3)"""

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".



c = (np.transpose(b,(1,2,0)))

"""
print(c)

c = b.T
"""
#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c

"""
d = np.add(a, c))


print(d)

print(a.shape)

print(d.shape)

Funciona por que las dos matrices son del mismo shape.
"""

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

"""
print(a)
print("-"*15)
print(d)
print("-"*15)

print(a.size)
print(d.size)

print(a.shape)
print(d.shape)

Explicación: ambas poseen el mismo tamaño (30 elementos) y ambas poseen la misma forma (2, 3, 5).

"""
#12. Multiply a and c. Assign the result to e.

e = a * c

"""
e1 = np.multiply(a,c)

print(e)

print("-"*25)

print(e1)
"""

#13. Does e equal to a? Why or why not?

"""
print(e == a)

Explicación: las dos variables son exactamente iguales. La variable A es la genunina y la variable e es la multiplicación por 1 de a.



print(e)
print("-"*20)
print(a)
"""


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


dup = []
for k in d:
    for i in k:
        for h in i:
                dup.append(h)

d_max = max(dup)
d_min = min(dup)
d_mean = sum(dup) / len(dup)

"""
print(d_max)
print(d_min)
print(d_mean)
"""

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.


f = np.empty((2,3,5))

print(f)

"""
"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
"""

If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.

"""
"""
for key,value in enumerate(d):
        if (value > d_min) & (value < d_mean):
                print(key,25)
        if (value > d_mean) & (value < d_max):
                print(key,75)
        if (value == d_mean):
                print(key,50)
        if (value == d_min):
                print(key,0)
        if (value == d_max): # or else
                print(key,100)


f [(d > d_min) & (d < d_mean)] = 25
f [(d > d_mean) & d < d_max] = 75
f [(d == d_mean)] = 50
f [(d == d_min)] = 0
f [(d == d_max)] = 100
"""


#17. Print d and f. Do you have your expected f?
"""
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



# creo que tiene que ser algo así, pero no entiendo exactamente.

"""
f [(d > d_min) & (d < d_mean)] = B
f [(d > d_mean) & d < d_max] = D
f [(d == d_mean)] = C
f [(d == d_min)] = A
f [(d == d_max)] = E
"""