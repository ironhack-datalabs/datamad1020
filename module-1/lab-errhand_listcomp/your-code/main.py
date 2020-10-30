#Example: 

"""eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)
"""

#Insert here the module/library import statements 
import math
import re
import random
import sys
import time
import os.path 




print("ejercicio\n")
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
square = [i**2 for i in range(1,21)]
print(square)
print("---------------------------------------------------------")



print("ejercicio2\n")
#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
power_of_two = [2**i for i in range(1,51)]
print(power_of_two)
print("---------------------------------------------------------")	


print("ejercicio3\n")
#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
sqrt = [math.sqrt(i) for i in range( 1,101)]
print(sqrt)
print("---------------------------------------------------------")



print("ejercicio4\n")
#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
my_list = [i for i in range(-10,1)]
print(my_list)
print("---------------------------------------------------------")

print("ejercicio5\n")
#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [i for i in range(1,101,2)]
print(odds)
print("---------------------------------------------------------")



print("ejercicio6\n")
#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [i for i in range(1,1001) if i%7 == 0]
print(divisible_by_seven)
print("-----------------------------------------------------------")



print("ejercicio7\n")
#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find All of the words in a string that are monosyllabic'
lista_vocales = ["a","e","i","o","u"]
non_vowels = [i for i in teststring if i.lower() not in lista_vocales] 
print(non_vowels)
print("-------------------------------------------------------------------")





print("ejercicio8\n")
#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

cadena = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [i for i in cadena if i == i.capitalize()]
print(capital_letters)
print("----------------------------------------------------------------")
	
#bien hasta aqui

print("ejercicio9\n")
#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

cadena2 = 'The quick brown fox jumped over the lazy dog'
vocals = ["a","e","i","o","u"]
consonants = [i for i in cadena2 if i.lower() not in vocals]
print(consonants)
print("------------------------------------------------------------------")


print("ejercicio10\n")
#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results. path relativos path absoluto, mejor con path relativos
contenido = os.listdir("../../../../")
print(contenido)  #No se si era esto lo que se pedía la verdad...



print("-----------------------------------------------------------------------------------")


print("ejercicio11\n")
#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
random_lists = [[random.randint(0,101) for i in range(10)],[random.randint(0,101) for i in range(10)],
[random.randint(0,101) for i in range(10)],[random.randint(0,101) for i in range(10)]]
print(random_lists)
print("-------------------------------------------------------")



print("ejercicio12\n")
#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [x for i in list_of_lists for x in i]
print(flatten_list)
print("---------------------------------------------------------")



print("ejercicio13\n")
#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.


list_of_lists1 = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(x) for i in list_of_lists1 for x in i]
print(floats)
print("-------------------------------------------")


print("ejercicio14\n")
#14. Handle the exception thrown by the code below by using try and except blocks. 
"""
try:
	for i in ['a','b','c']:
		print(i**2)
except TypeError:
	print("No se puede elevar un string al cuadrado, debe ser un numero.") #ME APARECIA SIN PARENTESIS EN EL PRINT, TB PERO ME RESULTO IMPOSIBLE, 
	                                                                        NO ME IMPRIMIA EL ERROR CREADO NO SE PORQUÉ


"""    	
print("---------------------------------------------------------------------\n")




print("ejercicio15\n")
#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0
try:
	z = x/y
except ZeroDivisionError:
	print("No se puede dividir por cero")
finally:
	print("All Done")
print("------------------------------------------------------------")




print("ejercicio16\n")
#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]
try:
	print(abc[3])
except IndexError:
	print("l elemento 3 no existe, el rango va de 0 a 2 inclusive")
	print("--------------------------------------------")


print("ejercicio17\n")
#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 

"""

try:
	n1 = int(input("Introduce un numero: "))
	n2 = int(input("Introduce otro numero: "))

	c = n1/n2
	print(c)
         
except ZeroDivisionError:
	print("No se puede dividir un numero por 0\n")
except ValueError:
	print("Debe introducir un numero\n")
finally:
	print("Se acabo el programa")
	print("----------------------------------------")

"""
print("--------------------------------------------------------------")
print("ejercicio18\n")
#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

try:
	f = open('testfile','r')
	f.write('Test write this')

except FileNotFoundError:
	print("Especifica la ruta del achivo para poder utilizarlo.")
	print("--------------------------------------------------")




print("ejercicio19\n")
#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int

try:
	fp = open('myfile.txt')
	line = f.readline()
	i = int(s.strip())
except FileNotFoundError:
	print("Especifica la ruta del archivo, porque no se puede convertir a int un archivo que no existe")
print("---------------------------------------------")

print("ejercicio20\n")   
#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

"""
def linux_interaction():
	assert ('linux' in sys.platform), "Function can only run on Linux systems."
	print('Doing something.')

try:	
	linux_interaction()
except AssertionError:
	print("Function can only run on Linux systems.\n")

finally:
	time.sleep(0.5)
	print("Y...")
	time.sleep(1)
	print("Se acabo lo que se daba ;)")
print("------------------------------------------------------")

"""
print("----------------------------------------------------------------")


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions
print("ejercicio21\n")
#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.


"""
def square():
	while True:
		try:
			n = int(input("Ingrese un numero entero: "))
		except ValueError:
			print("\n                  DEBE SER UN NUMERO, INTENTELO DE NUEVO!!!!!!!!!!!!!!!!!")
			
		else:
			print(f"\n  --------------------------El cuadrado del numero {n} es {n**2} ;)-------------------------------")
			break


square()
"""


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 

#No entendi el enunciado muy bien, haber si me dices como es porque me destroce la cabeza con este

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

"""
class ExcesoNumericoError(Exception):
	pass

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))
if Num_of_Sections > 2:
	raise ExcesoNumericoError("EL NUMERO DE SECCIONES DEBE SER MENOR QUE DOS")
"""

	






