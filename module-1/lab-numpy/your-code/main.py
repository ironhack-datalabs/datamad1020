#1. Import the NUMPY package under the name np.

import numpy as np



#2. Print the NUMPY version and the configuration.



print(np.__version__)


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))


#formas de utilizar random:
#la forma de antes
#ejemplo  np.random.rand(4,2) 
#ejemplo np.random.randint(10)


#4. Print a.
print(a)
print("------------------------------------------------------------")




#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))



#6. Print b.

print(b)
print("-------------------------------------------------------------------------------")



#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size == b.size)
print("------------------------------------------------------------------------")
#Si , da True



#8. Are you able to add a and b? Why or why not?



# No, porque no se relacionan las posiciones de los elementos de la matriz a con la de la matriz b, tienen diferentes shapes.


#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = b.reshape(2,3,5)

print(a.shape == c.shape)
print("---------------------------------------------------")




#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d = a + c

"""
funciona porque ahora tienen la misma estructura y al ser así, ya se puede sumar entre los elemenos de cada una por tener 
la misma distribución matricial, mismas filas, mismas columnas, misma dimension... mismos shapes vamos.

""" 




#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print("ejercicio 11")
print("matriz A ----------------------------------------------------------------")
print(a,"\n")
print("matriz d-----------------------------------------------------------------")
print(d)

"""La relacion es que al sumar la matriz a con la c, en la de matriz D, se han generado los resultados de sumar cada elemento de la matriz uno con el de la matriz
c, y como la c tenia todo valores de uno, la matriz D tiene un 1 sumado a cada valor de matriz A."""
print("---------------------------------------------------------------------------------")



#12. Multiply a and c. Assign the result to e.
e = a*c



#13. Does e equal to a? Why or why not?


#Todo valor multiplicado por uno da el mismo valor, y si multiplicados todos los valores de A por 1, nos va a dar la misma matriz A.





#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"


d_max = d.max()
d_min =  d.min()
d_mean = d.mean()
print(f"{d_max} es el valor maximo de D")
print(f"{d_min} es el valor minimo de D")
print(f"{d_mean}es el valor medio de D")

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`
print("-----------------------------------------------------")

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
for i in d:
    for z in i:
        for x in z:
            if x > d_min and x < d_mean:
                f = np.append(f,25)
            elif x > d_mean and x < d_max:
                f = np.append(f,75)
            elif  x == d_mean:
                f = np.append(f,50)
            elif x == d_min:
                f = np.append(f,0)
            elif x == d_max:
                f = np.append(f,100)


print(f)
print("-------------------------------------------------------------")
print("ejercicio 17")

 


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

print("esto es d y abajo el f")   #YA SE QUE NO ES LO QUE PIDE EL EJERCICIO, ME SALE PERO EN UNA MISMA LISTA TODO Y NO POR SEPARADO, NO SABÍA COMO HACERLO
print(f)

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

z = np.empty((2,3,5),dtype= str)

for o in d:
    for w in o:
        for c in w:
            if c > d_min and c < d_mean:
                z = np.append(z,"B")
            elif c > d_mean and c < d_max:
                z = np.append(z,"D")
            elif  c == d_mean:
                z = np.append(z,"C")
            elif c == d_min:
                z = np.append(z,"A")
            elif c == d_max:
                z = np.append(z,"E")


print("----------------------------------------------------------------------")
#SE QUE NO ESTA BIEN PERO IMAGINO QUE SERA PONIENDO QUE SEA DE TIPO STRING ESA MATRIZ VACIA PARA PODER INSERTAR STRINGS Y QUE SE RECONOZCAN PERO IGUAL SALE TODO JUNTO
#YA ME DIRAS COMO SE HACE MAKINA

print(z)




