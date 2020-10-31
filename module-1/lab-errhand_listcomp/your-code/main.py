# #Example: 
eggs = (1,3,8,3,2)
my_listComprehension = [1/egg for egg in eggs]
print(my_listComprehension)

# #Insert here the module/library import statements 
import math as m
import re
import string
import os
import random
import sys

# #1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# # Remember to use list comprehensions and to print your results
square = [x ** 2 for x in range(20)]
print(square)

# #2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# # Remember to use list comprehensions and to print your results
power_of_two = [2 ** x for x in range(50)]
print(power_of_two)

# #3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# # You will probably need to install math library with pip and import it in this file.  
# # Remember to use list comprehensions and to print your results
sqrt = [m.sqrt(x) for x in range(100)]
print(sqrt)

# #4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# # Remember to use list comprehensions and to print your results
my_list = [n for n in range(-10, 1, 1)]
print(my_list)

# #5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# # Remember to use list comprehensions and to print your results
odds = [n * 2 for n in range(1, 51)]
# odds2 = [n for n in range(1, 101) if n % 2 == 0]
print(odds)

# #6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# # Remember to use list comprehensions and to print your results
divisible_by_seven = [n for n in range(1, 1001) if n % 7 == 0]
print(divisible_by_seven)
# divisible_by_seven2 = [n * 7 for n in range(1, 143)]
# print(divisible_by_seven == divisible_by_seven2)

# #7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# # Remember to use list comprehensions and to print your results
# # You can use the following test string but feel free to modify at your convenience
vowels =  'aeiouAEIOU'
teststring = 'Find all of the words in a string that are monosyllabic'
non_vowels = [s for s in teststring if s not in vowels]
print(non_vowels, ''.join(non_vowels))

non_vowels_2 = re.findall(r"[^aeiouAEIOU]+", teststring)
print(non_vowels_2)

# #8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# # Use capital_letters as the name of the list.  
# # Remember to use list comprehensions and to print your results
sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = re.findall(r"[A-Z]+", sentence)
print(capital_letters)

# #9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# # Use consonants as the name of the list.
# # Remember to use list comprehensions and to print your results.
consonants = [c for c in sentence if c not in vowels]
# consonants = re.findall(r"[^aeiouAEIOU]+", sentence)
print(consonants)

# #10. Find the folders you have in your madrid-oct-2020 local repo. Use files as name of the list.  
# # You will probably need to import os library and some of its modules. You will need to make some online research.
# # Remember to use list comprehensions and to print your results.
abs_path = '/Users/gerardovitaleerrico/Documents/datamad1020/module-1/lab-errhand_listcomp'
rel_path = '../../'
datamad1020 = os.listdir('../../')
print(datamad1020)

# #11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
# #You will probably need to import random module
# # Remember to use list comprehensions and to print your results
random_lists = [[random.randint(0,100) for _ in range(11)] for _ in range(4)]
print(random_lists, len(random_lists))

# #12. Flatten the following list of lists. Use flatten_list as the name of the output.
# # Remember to use list comprehensions and to print your results
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [
    i 
    for lst in list_of_lists
    for i in lst
]
print(flatten_list)

# #13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# # Remember to use list comprehensions and to print your results.
list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]
floats = [[float(x) for x in n] for n in list_of_lists]
print(floats)

# #14. Handle the exception thrown by the code below by using try and except blocks. 
try:
    for i in ['a','b','c']:
        print(i ** 2)
except TypeError:
    print('There is an error (TypeError)')

# #15. Handle the exception thrown by the code below by using try and except blocks. 
# #Then use a finally block to print 'All Done.'
# # Check in provided resources the type of error you may use. 
x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print('There is an error!')
finally:
    print('All Done.')    

# #16. Handle the exception thrown by the code below by using try and except blocks. 
# # Check in provided resources the type of error you may use. 
try:
    abc=[10, 20, 20]
    print(abc[3])
except IndexError:
    print('There is an error!')

# #17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# # Hint: take a look on python input function. 
# # Check in provided resources the type of error you may use. 
# try:
#     a = int(input('provide an number: '))
#     b = int(input('provide another one: '))
# except ValueError:
#     print("You havn't provided an integer")
# except ZeroDivisionError:
#     print("You'r trying to devide a number by 0, that's not possible")

# #18. Handle the exception thrown by the code below by using try and except blocks. 
# # Check in provided resources the type of error you may use. 
try:
    f = open('testfile','r')
    f.write('Test write this')
except FileNotFoundError:
    print("there's not such a file.")

# #19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
# #Hint: the file could not exist and the data could not be convertable to int
try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())
except FileNotFoundError:
    print("there's not such a file.")
except ValueError:
    print("You havn't provided a number")

# #20. The following function can only run on a Linux system. 
# # The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# # Handle this exception using try and except blocks. 
# # You will probably need to import sys 

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except AssertionError:
    pass

# # Bonus Questions:
# # You will need to make some research on dictionary comprehension to solve the following questions

# #21.  Write a function that asks for an integer and prints the square of it. 
# # Hint: we need to continually keep checking until we get an integer.
# # Use a while loop with a try,except, else block to account for incorrect inputs.
def x_square():
    while True:
        try:
            x = float(input('provide a number, so the function can print the square of it: '))
            return x ** 2
        except ValueError:
            print("you haven't provided a number, please try again.")
            continue
        else:
            return x ** 2
print(x_square())

# # 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9).
# # Use results as the name of the list
# # You have the following user inputs and the Num_of_sections can not be less than 2.

# # 23. Define a customised exception to handle not accepted values.
# # Hint: Create a class derived from the pre-defined Exception class in Python

# Total_Marks = int(input("Enter Total Marks Scored: "))

class OutOfRangeError(Exception):
    def __init__(self, number, errormessage='''Raised when the input provided is out of the range established'''):
        self.number = number
        self.errormessage = errormessage
        super().__init__(self.errormessage)

def handling_input():
    try:
        Num_of_Sections = int(input("Enter Num of Sections: "))
        if Num_of_Sections < 2 or Num_of_Sections > 9:
            raise OutOfRangeError(Num_of_Sections)
    except ValueError:
        print('A number between 2 and 9 must be provided.')
    else:
        return Num_of_Sections

def divisible():
    Num_of_Sections = handling_input()
    return [n for n in range(1,1000) if n % Num_of_Sections == 0]

print(divisible())