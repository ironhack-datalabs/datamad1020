#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import math
import re
import os
import random
import sys

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
print("Exercise 1")

#square = []
#for n in range (21):
#    square.append(n**2)
#    print(square)

square =[n**2 for n in range(21)]
print(square)

#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
print("Exercise 2")

power_of_two = [n**2 for n in range(51)]
print(power_of_two)

#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
print("Exercise 3")

sqrt = [n**0.5 for n in range(101)]
print(sqrt)

#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
print("Exercise 4")

my_list = [n for n in range(-10,1)]
print(my_list)

#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
print("Exercise 5")

odds = [n for n in range(1,101) if n%2 != 0]
print(odds)

#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
print("Exercise 6")

divisible_by_seven = [n for n in range(1,1001) if n%7 == 0]
print(divisible_by_seven)

#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
print("Exercise 7")

teststring = 'Find all of the words in a string that are monosyllabic'
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
non_vowels = [i for i in teststring if i not in vowels]
print(non_vowels)
# or print(*non_vowels), unpacking a list

#another solution:
#non_vowels = re.findall(r"[^aeiouAEIOU]", teststring)
#print(non_vowels)

#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
print("Exercise 8")

sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [i for i in sentence if i.isupper() == True]
print(capital_letters)

#another solution:
#capital_letters = re.findall(r"[A-Z]", sentence)
#print(capital_letters)

#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
print("Exercise 9")

sentence = 'The Quick Brown Fox Jumped Over The Lazy Dog'
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
consonants = [i for i in sentence if i not in vowels]
print(consonants)

#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
print("Exercise 10")

files = [x for x in os.listdir(path = "/Users/ale/datamad1020")]
print(files)

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
print("Exercise 11")

#random.randint(0,100)


#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results
print("Exercise 12")

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [n for sublist in list_of_lists for n in sublist]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.
print("Exercise 13")

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(n) for sublist in list_of_lists for n in sublist]
print(floats)

#14. Handle the exception thrown by the code below by using try and except blocks. 
print("Exercise 14")

try:
    for i in ['a','b','c']:
        print(i**2)

except TypeError:
    print("Strings cannot be squared")

#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
print("Exercise 15")

x = 5
y = 0

try:
    z = x/y
    print(z)
except:
    print("ZeroDivisionError: division by zero")


#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Exercise 16")

abc=[10,20,20]
try:
    print(abc[3])
except IndexError:
    print("List of index out of range")

#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
print("Exercise 17")

try:
    x = int(input("Enter the first number (dividend):"))
    y = int(input("Enter the second number (divisor):"))
    print(x/y)
except ZeroDivisionError:
    print("ZeroDivisionError: No dividing by zero")
except ValueError: # try...catch
    print("ValueError: Could not operate. Please input integers or floats.")

#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print("Exercise 18")

try:
    f = open('testfile','r')
    f.write('Test write this')

except FileNotFoundError:
    print("No such file or directory: {f}")


#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
print("Exercise 19")

try:
    fp = open('myfile.txt')
    line = f.readline()
    i = int(s.strip())

except FileNotFoundError:
    print("No such file or directory.")
except ValueError:
    print("The data cannot be convertable to an integer.")

#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
print("Exercise 20")

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')


# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
print("Exercise 21")




# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
print("Exercise 22")
'''
results = []
for n in range(1,1000):
    is_divisible_by_range = True
    for x in range(1,10):
        if n%x != 0:
            is_divisible_by_range = False
            break
    if is_divisible_by_range:
        results.append(n)
'''
results = []
for n in range(1,1000):
    cont = 0
    for x in range(1,10):
        if n%x ==0:
            cont += 1
    if len(range(1,10)) == cont:
        results.append(n)
print(results)

'''

# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python
print("Exercise 23")

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))


'''