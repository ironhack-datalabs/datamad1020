

#Example: 

"""
eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)
"""

#Insert here the module/library import statements 

import random 
import math
import os
import random
import pandas

"""from os import dir"""



#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

""" 1. Calcula el cuadrado de los primeros 20 números. Utilice cuadrado como nombre de la lista.
   Recuerde usar listas por comprensión e imprimir sus resultados


square = [i**2 for i in range(0,21)]

print(square)
"""

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

""" 2. Calcula las primeras 50 potencias de dos. Utilice power_of_two como el nombre de la lista.
    Recuerde usar listas por comprensión e imprimir sus resultados

power_of_two = [2**i for i in range(0,51)]

print(power_of_two)
"""

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

""" 3. Calcula la raíz cuadrada de los primeros 100 números. Utilice sqrt como nombre de la lista.
    Probablemente necesitará instalar la biblioteca matemática con pip e importarla en este archivo.
    Recuerde usar listas por comprensión e imprimir sus resultados

# Opción 1:

sqrt = [i*0.5 for i in range(0,101)]

print(sqrt)

# Opción 2:

sqrt = [math.sqrt(i) for i in range(0,101)]

print(sqrt)
"""


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results

""" 
my_list = [i*-1 for i in reversed(range(0,11))]

print(my_list)
"""

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

"""
odds = [i for i in range(0,101) if i%2 !=0]

print(odds)
"""

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
"""
for i in range(0,1001):

    if i%7 == 0:
        print(i)

divisible_by_seven = [i for i in range(0,1001) if i%7 == 0]

print(divisible_by_seven)
"""
#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

"""
teststring = 'Find all of the words in a string that are monosyllabic'

vowels = ['a', 'e', 'i', 'o', 'u', ' ']

non_vowels = [i for i in teststring if i not in vowels]
print(non_vowels)

"""

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

text = "The Quick Brown Fox Jumped Over The Lazy Dog"

"""
capital_letters = [letters for letters in capital if letters[0] == letters.isupper()]

print(capital)

for letter in text:
    if letters[0] == letters.isupper():
        print(letters)

for letters in capital.split:
    if letters[0]:
        print(letters.isupper())


----> txt.upper()
# upper() method converts all lowercase characters in a string into uppercase characters and returns it
# estructura: string.upper()


uppers = []
lowers = []

for word in capital:
    uppers.append(word) if word[0].isupper()

print(uppers)

"""


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

"""
text1 = "The quick brown fox jumped over the lazy dog"
vowels = ['a', 'e', 'i', 'o', 'u', ' ']
consonats = [letter for word in text1 for letter in word if letter not in vowels]
print(consonats)
"""

#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
"""
import os 

print(os.getcwd()) # Para obtener el pwd normal

files = os.listdir(path="../../../")

print(files)
"""

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

"""
lst1 = []
lst2 = []
lst3 = []
lst4 = []

for i in random.randint(range(0,101,10)):
    lst1.append(i)
    lst2.append(i)
    lst3.append(i)
    lst4.append(i)

print(lst1)
print(lst2)
print(lst3)
print(lst4)
random_lists = [i for i in random.randrange(range(0,101,10))]"""

#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

"""
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

for list1 in list_of_lists:
    for list2 in list1:
        print(list2)

flatten_list2 = [list2  for list1 in list_of_lists for list2 in list1]

print(flatten_list2)
"""

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

"""
for lista1 in  list_of_lists:
    for lista2 in lista1:
        print(lista2)

floats = [float(lista2) for lista1 in  list_of_lists for lista2 in lista1 ]  

print(floats)
"""

#14. Handle the exception thrown by the code below by using try and except blocks. 

"""
for i in ['a','b','c']:
    print i**2

 

try:
    for i in ['a','b','c']:
        print (i**2)

except:
    print("The even_number function errored out.")

"""

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

"""
z = x/y

print(type(z))

 
try:
    z = x/y

except:
    print("No puedes dividir entre 0 melón ")

finally:
    print("All done") 
"""

#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

""" 
abc=[10,20,20]
 
try:
    print(abc[3]) 

except:
    print("Your list index out of range, pero puede seguir")

"""

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 




#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
"""
f = open('testfile','r')
f.write('Test write this')
"""


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

"""
fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
"""



#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

"""
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
"""

# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 




# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

"""
Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))

"""
