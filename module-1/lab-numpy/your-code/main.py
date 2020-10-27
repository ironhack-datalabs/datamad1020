#1. Import the NUMPY package under the name np.
import numpy as np


#2. Print the NUMPY version and the configuration.
print(np.version.version)
"""
1.19.1
"""

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
a = np.random.random( (2,3,5) )

"""
or np.random.randint(1,21, size=(2,3,5)) with integers, 
or an uniform distribution between 2 values np.random.uniform(1,21,(2,3,5)) (between 1 and 21)
or using a binomial distribution of the probability (ej np.random.binomial(5,0.4,(2,3,5)) with n=5 and p=0.4 )
or a normal distibution (ej np.random.normal(10,2, (2,3,5)) with mean=10 and sigma=2  )
(there are more probability distributions)
"""
#4. Print a.

"""
>>>print(a)
[[[0.39422839 0.13876125 0.80161223 0.07770237 0.51170142]
  [0.35588687 0.37976775 0.09785462 0.22581034 0.99098123]
  [0.42193473 0.3826454  0.9466472  0.72383606 0.45470496]]

 [[0.50248269 0.19298311 0.97261862 0.22534237 0.43246818]
  [0.24914785 0.60747931 0.04913475 0.15016942 0.04014943]
  [0.04159562 0.21899372 0.1525856  0.02472944 0.39853116]]]
"""

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.ones((5,2,3))

#6. Print b.
"""
>>>>print(b)

[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]
"""
#7. Do a and b have the same size? How do you prove that in Python code?
"""
>>>> np.size(a)==np.size(b)
True

The size is size(a) = size(b) = 30

"""


#8. Are you able to add a and b? Why or why not?
"""
No, because the shape of a and b is not the same. The size is the same but the important
thing is the shape to be added. 
"""

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".
c = np.transpose(b, (1,2,0) )

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?
d = a+c
"""
Now it works because the shape of a is the same as b (and hence the size of course)
"""

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.
print(a)
print(d)
"""
>>> print(a)
[[[0.39422839 0.13876125 0.80161223 0.07770237 0.51170142]
  [0.35588687 0.37976775 0.09785462 0.22581034 0.99098123]
  [0.42193473 0.3826454  0.9466472  0.72383606 0.45470496]]

 [[0.50248269 0.19298311 0.97261862 0.22534237 0.43246818]
  [0.24914785 0.60747931 0.04913475 0.15016942 0.04014943]
  [0.04159562 0.21899372 0.1525856  0.02472944 0.39853116]]]

>>>> print(d)
[[[1.39422839 1.13876125 1.80161223 1.07770237 1.51170142]
  [1.35588687 1.37976775 1.09785462 1.22581034 1.99098123]
  [1.42193473 1.3826454  1.9466472  1.72383606 1.45470496]]

 [[1.50248269 1.19298311 1.97261862 1.22534237 1.43246818]
  [1.24914785 1.60747931 1.04913475 1.15016942 1.04014943]
  [1.04159562 1.21899372 1.1525856  1.02472944 1.39853116]]]


As c is a matrix filled with ones with the same shape as a, d=a+c
each cell in c is the corresponding cell in a plus 1.
"""

#12. Multiply a and c. Assign the result to e.
e = a * c


#13. Does e equal to a? Why or why not?
"""
>>> e == a
array([[[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]],

       [[ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True],
        [ True,  True,  True,  True,  True]]])

When I try e == a, it shows a boleean for checing if each invidual cells in e are 
equal to the one with a. All of them are true. Clearly, a=e as if we multyply 2
matrix with the same shape, the result is the product of the values of each cell.

As c is a matrix with ones, a*c=e -> a=e

"""
#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"
d_max=d.max()
d_min=d.min()
d_mean=d.mean()
"""
I stored the result in the asked variables, but here I print the max, min and mean 

>>>> d.max(),d.min(),d.mean()
(1.9909812336835477, 1.0247294411770764, 1.372082870145217)
"""

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.
f = np.empty(np.shape(d))



"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""
#This exercisa can be done in only one line
f = ((d < d_mean) & (d> d_min))*25  + ((d > d_mean) & (d<d_max))*75 + (d == d_min)*0 + (d == d_max)*100 + (d ==d_mean)*50



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
#My resut:
"""
The result of the print is the following:

>>>print(f)
[[[ 75  25  75  25  75]
  [ 25  75  25  25 100]
  [ 75  75  75  75  75]]

 [[ 75  25  75  25  75]
  [ 25  75  25  25  25]
  [ 25  25  25   0  75]]]
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
print(str(f).replace("100","E").replace("75","D").replace("50","C").replace("25","B").replace("0","A"))
"""
[[[ D  B  D  B  D]
  [ B  D  B  B E]
  [ D  D  D  D  D]]

 [[ D  B  D  B  D]
  [ B  D  B  B  B]
  [ B  B  B   A  D]]]
"""
