#Example: 
'''
eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)'''

#Insert here the module/library import statements 

import pandas as pd
import numpy as np
import math
import string
import os
import random
import sys
import re
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
numbers= list(range(1, 200))
'''
square=[x**2 for x in numbers if x<=20]
print(square)
'''

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
'''
power_of_two=[x**2 for x in numbers if x<=50]
print(power_of_two)
'''
#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
'''
sqrt=[x**0.5 for x in numbers if x<=100]
print(sqrt)
'''
#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
'''
my_list=[x for x in range(-10,1)]
print(my_list)
'''
#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
'''
odds=[number for number in range(1,101) if number%2!=0]
print(odds)
'''
#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
'''
divisible_by_seven=[numbers for numbers in range(1,1001) if numbers%7==0]
print(divisible_by_seven)
'''

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
'''
teststring = 'Find all of the words in a string that are monosyllabic'

non_vowels=[]
for word in teststring:
    for letter in word:
        if letter not in ["a","e","i","o","u"]:
            non_vowels.append(letter)

non_vowels=[letter for letter in teststring if letter not in ["a","e","i","o","u"]]

print(non_vowels)
'''
#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
'''
string='The Quick Brown Fox Jumped Over The Lazy Dog'

capital_letter=re.findall(r"[A-Z]", string)
print(capital_letter)
'''

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
'''
string='The quick brown fox jumped over the lazy dog'

consonants=[letter for word in string for letter in word if letter in ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]]
print(consonants)
'''
#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
'''
print(os.getcwd())
files=os.listdir(path="../../../")
print(files)
'''
#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
'''
randomlist1 = []
randomlist2= []
randomlist3= []
randomlist4= []
for i in range(0,10):
    number = random.randint(1,101)
    randomlist1.append(number)
    number = random.randint(1,101)
    randomlist2.append(number)
    number = random.randint(1,101)
    randomlist3.append(number)
    number = random.randint(1,101)
    randomlist4.append(number)
random_lists=[randomlist1, randomlist2, randomlist3, randomlist4]
print(random_lists)
'''
'''
random_lists=[i for i in random.randint(1,101,10)]
print(random_lists)
'''
'''
random_lists=[[randomlist1, randomlist2, randomlist3, randomlist4] for i in range(0,10) number = random.randint(1,101) randomlist1.append(number) 
number = random.randint(1,101) randomlist2.append(number) number = random.randint(1,101) randomlist3.append(number) number = random.randint(1,101)
randomlist4.append(number)]
'''
#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results
'''
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list=[element for lst1 in list_of_lists for element in lst1]
print(flatten_list)
'''
#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.
'''
list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats=[float(element) for lst1 in list_of_lists for element in lst1]
print(floats)
'''
#14. Handle the exception thrown by the code below by using try and except blocks. 
'''
try:
    for i in ['a','b','c']:
        print (i**2)
except TypeError:
    print("Could not operate with strings")

'''
#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
'''
try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError:
    print("It is not possible to divide by zero")
finally:
    print("All Done")
'''



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
'''
try:
    abc=[10,20,20]
    print(abc[3])
except IndexError:
    print("The index provided for the list is not valid")
'''
#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
'''
num1=input("Enter the first number for the division ")
num2=input("Enter the second number ")
try:
    division=float(num1)/float(num2)
    print(division)
except ZeroDivisionError:
    print("You can not divide by zero")
except ValueError:
    print("You have to introduce a number to do the division")
'''

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

'''
try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("The file could not be found")
'''


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
'''
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("That file was not found")
except ValueError:
    print("The data can not be converted to int")
'''


#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
'''
try:
    def linux_interaction():
        assert ('linux' in sys.platform), "Function can only run on Linux systems."
        print('Doing something.')
except Exception as err:
    print("Ths function can not run in a system other than Linux")
'''
# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
'''
number=input("Write an integer for the calculation ")
def integers (number):
    
    try:
        number=input("Write an integer for the calculation ")
        number_sqr=int(number)**2
    except ValueError as err:
        print("Choose another number ")
        number=input("Write an integer for the calculation ")
    else:
        print(number_sqr)

integers(number)
'''


# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
'''
results=[]
for numbers in range(1,1001):
    for div in range(2,10):
        if numbers%div==0:
            results.append(numbers)
print(results)
'''
# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
'''
Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))

class NotAccepted (Exception):
    def __init__(self,Total_Marks, Num_of_Sections):
        self.Total_Marks= Total_Marks
        self.Num_of_Sections =Num_of_Sections
        if (Total_Marks != [0,1,2,3,4,5,6,7,8,9]) or (Num_of_Sections != [0,1,2,3,4,5,6,7,8,9]):
            print("You have to introduce a number")
        elif Num_of_Sections<2:
            print("The Num of Sections should be higher tan 2")
        
'''
