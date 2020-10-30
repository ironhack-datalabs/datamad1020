#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import numpy as np
import string
import random 
import sys 
import os
#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results

square = [ x**2 for x in range(1,21) ]


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results

power_of_two =  [ 2**x for x in range(1,51) ]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results

sqrt =  [ np.sqrt(x) for x in range(1,101) ]
print(sqrt)


#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results


#Different forms of doing the same
my_list = [-x for x in range(10,-1,-1)]
my_list = [x for x in range(-10,1)]


#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results

odds = [x for x in range(1,101) if x%2==1]


#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results

divisible_by_seven = [x for x in range(1,1001) if x%7==0]


#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience

teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [letter for letter in teststring if letter.lower() not in ["a","e","i","o","u"]]


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results

teststring = 'The Quick Brown Fox Jumped Over The Lazy Dog'
#As we must find all the capital letters, I understand that I have to list all the unique capital letters
#so I used a set. It is not the same as remove all lowercase letters
capital_letters = {letter for letter in teststring if letter in string.ascii_uppercase}


#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.

teststring = 'The Quick Brown Fox Jumped Over The Lazy Dog'
#As we must find all the consonants, I used a set, as this is not as ex. 7, to remove the vowels. We
#must create a set with all the different consonants.
consonants = {letter.lower() for letter in teststring if letter.lower() in set(string.ascii_lowercase) - {"a","e","i","o","u"}}


#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.

#The name of the folder I assumed that is "datamad1020", but the name is not necesary. I assumed as well that
#the location is the equivalent as "datamad1020", and my cwd obtained with os.getcwd() is
#/home/ordovas/IRONHACK/labs/datamad1020/module-1/lab-errhand_listcomp/your-code'
files = os.listdir(path="../../../")


#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results

random_lists = [ [random.randint(0, 100) for _ in range(10)] for _ in range(4) ]


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]

flatten_list = [el for lst in list_of_lists for el in lst]

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

#floats = [[ ] for lst in  list_of_lists ]
floats = [[float(el) for el in lst] for lst in list_of_lists]

#14. Handle the exception thrown by the code below by using try and except blocks. 


for i in ['a','b','c']:
    try:
        print(i**2)
    except:
        print("You can't compute the square number of a str!")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 

x = 5
y = 0

try:
    z = x/y
except:
    print("I'm not going to divide anything by 0...")
finally:
    print("All Done.")



#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 

abc=[10,20,20]


try:
   print(abc[3])
except IndexError:
    print("Wrong index... Remember that the first index in python is 0!")
    
#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 


try:
    n1=float(input("Choose one positive number for the dividend: "))
    n2=float(input("Choose another positive number for the divisor:  "))
    if (n1<0) or (n2<0):
        raise TypeError
    divis = n1 / n2
    print(divis)
except ZeroDivisionError:
    print("Why would you want to divide by 0? You must be an evil being.")
except TypeError:
    print("POSITIVE NUMBERS! >:(")
except ValueError:
    print("No, no, no... you must divide NUMBERS!")


#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("The file or directory is requested but doesn’t exist! Solve this, punk.")
except IOError: #MacOS
    print("The file or directory is requested but doesn’t exist! Solve this, punk.")



#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())

except FileNotFoundError:
    print("The file or directory is requested but doesn’t exist! Solve this, punk.")
except ValueError:
    print("The stuff you want to convert to int is impossible!")    
except UnicodeDecodeError:
    print("That's some weird characters you want me to work with...")
except NameError:
    print("The name of the variables are wrong. Check your code...")

#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
     
try:
    linux_interaction()
except AssertionError:
    print("You don't have a linux plataform, so this function is forbiden to you!")

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

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


