#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print("-------------------------- EJERCICIO 2 -------------------------------")
print(np.version.version)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.rand(2,3,5)
a = np.random.randn(2,3,5)
a = np.random.random((2,3,5))

#4. Print a.
print("-------------------------- EJERCICIO 4 -------------------------------")
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
b = np.ones((5,2,3))


#6. Print b.
print("--------------------------EJERCICIO 6-------------------------------")
print(b)


#7. Do a and b have the same size? How do you prove that in Python code?
''' No tengo muy claro si con size se refiere efectivamente a la función size(numero de elementos) ,o a shape(dimensión). 
Pero bueno pongo los dos, que son cortitos. Tienen el mismo número de elementos, pero distinta dimensión. '''
print("--------------------------EJERCICIO 7-------------------------------")
print(f"Size de a igual al de b: {a.size == b.size}")
print(f"Shape de a igual al de b: {a.shape == b.shape}")



#8. Are you able to add a and b? Why or why not?
'''No, porque son elementos de dimensiones distintas y a diferencia del producto vectorial, la suma no genera una nueva dimensión.'''



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
''' 
Escribimos nuestra antigua posicion 0 (el 5) en el nuevo 0,
nuestra antigua posicion 1 (el 2) en el nuevo 1 y 
nuestra antigua posicion 2 (el 3) en el nuevo 2
'''
c = np.transpose(b, (1, 2, 0))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
'''Ahora se pueden sumar porque son de la misma dimension'''
d = a+c



#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
'''Se ha sumado elemento a elemento, es decir, Anxm + Cnxm. Ninguno de los elementos resultantes es mayor que 2 porque los 
valores random estaban entre 0 y 1. '''
print("--------------------------EJERCICIO 11-------------------------------")
print(a,"\n"*3,d)


#12. Multiply a and c. Assign the result to e.
e = a*c


#13. Does e equal to a? Why or why not?
'''Si, e es igual que a porque en una multiplicacion normal se multiplica elemento a elemento y como todos los valores de c son 1 pues e se queda igual.
Si la multiplicación fuese el producto matricial otro gallo cantaría. '''



#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max = d.max()
d_min = d.min()
d_mean = d.mean()



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
print("-------------------------- EJERCICIO 16 -------------------------------")
'''
if  d_min < d < d_mean  --->  75
if  d = d_mean asigno   --->  50
if  d = d_min asigno    --->   0
if  d = d_max           ---> 100
'''


'''
Vale con lo de abajo me he rayado mazo, era con lo de los masks de hoy, pero me gusta guardar mis rayadas sorry. 
Por cierto feliz cumpleaños camarada del 97.

arr = [n for arr in d for subarray in arr for n in subarray]
f_lst = []
for number in arr:
        if (number > d_min) & (number < d_mean):
                f_lst.append(75)
        elif number == d_mean:
                f_lst.append(50)
        elif number == d_min:
                f_lst.append(0)
        elif number == d_max:
                f_lst.append(100)
'''
f[(d > d_min) & (d < d_mean)] = 75
f[(d > d_mean) & (d < d_max)] = 25
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max ] = 100





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
print("-------------------------- EJERCICIO 17 -------------------------------")
print(f"ESTA ES d:\n {d}\n\n")
print(f"ESTA ES f:\n {f}")

''''''


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
print("-------------------------- BONUS -------------------------------")
#Se convierte f en un objeto y ya le ponemos lo que queramos
f = np.array(f,dtype=object)


f[(d > d_min) & (d < d_mean)] = 'A'
f[(d > d_mean) & (d < d_max)] = 'B'
f[d == d_mean] = 'C'
f[d == d_min] = 'D'
f[d == d_max ] = 'E'

print(f)