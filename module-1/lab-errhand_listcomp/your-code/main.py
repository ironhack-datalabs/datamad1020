#Example: 

eggs = (1,3,8,3,2)

my_listComprehension = [1/egg for egg in eggs]

print(my_listComprehension)

#Insert here the module/library import statements 
import re
import os,sys
import random

#1. Calculate the square number of the first 20 numbers. Use square as the name of the list.
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 1 -------------------------------------")
square = [n**2 for n in range(1,21)]
print(f"n^2 = {square}")


#2. Calculate the first 50 power of two. Use power_of_two as the name of the list.
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 2 -------------------------------------")
power_of_two = [2**e for e in range(1,51)]
print(f"Power of two = {power_of_two}")



#3. Calculate the square root of the first 100 numbers. Use sqrt as the name of the list.
# You will probably need to install math library with pip and import it in this file.  
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 3 -------------------------------------")
sqrt = [num**0.5 for num in range(1,101)]
print(f"x^2 = {sqrt}")




#4. Create this list [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0]. Use my_list as the name of the list.
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 4 -------------------------------------")
my_list = [n for n in range(-10,1)]
print(f"my_list = {my_list}")



#5. Find the odd numbers from 1-100. Use odds as the name of the list. 
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 5 -------------------------------------")
odds = [n for n in range(1,100) if n%2]
print(f"odds = {odds}")



#6. Find all of the numbers from 1-1000 that are divisible by 7. Use divisible_by_seven as the name of the list.
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 6 -------------------------------------")
divisible_by_seven = [n for n in range(1,1001) if not n%7]
print(f"divisible_by_seven = {divisible_by_seven}")



#7. Remove all of the vowels in a string. Hint: make a list of the non-vowels. Use non_vowels as the name of the list.
# Remember to use list comprehensions and to print your results
# You can use the following test string but feel free to modify at your convenience
print(f"------------------------------------- EJERCICIO 7 -------------------------------------")
teststring = 'Find all of the words in a string that are monosyllabic'
vowels = 'aeiouAEIOU'
non_vowels_list = [n for n in teststring if n not in vowels]
non_vowels = ''.join(non_vowels_list)
print(non_vowels)


#8. Find the capital letters (and not white space) in the sentence 'The Quick Brown Fox Jumped Over The Lazy Dog'. 
# Use capital_letters as the name of the list.  
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 8 -------------------------------------")
teststring = 'Find all of the words in a string that are monosyllabic'
vowels = 'aeiouAEIOU'
non_vowels_list = [n for n in teststring if n not in vowels]
non_vowels = ''.join(non_vowels_list)
print(non_vowels)




#9. Find all the consonants in the sentence 'The quick brown fox jumped over the lazy dog'.
# Use consonants as the name of the list.
# Remember to use list comprehensions and to print your results.
print(f"------------------------------------- EJERCICIO 9 -------------------------------------")
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = [n for n in string if n in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
print(capital_letters)

print(f"------------------------------------- EJERCICIO 9.1 -------------------------------------")
string = 'The Quick Brown Fox Jumped Over The Lazy Dog'
capital_letters = re.findall(r"[A-Z]", string)
print(capital_letters)



#10. Find the folders you have in your madrid-oct-2018 local repo. Use files as name of the list.  
# You will probably need to import os library and some of its modules. You will need to make some online research.
# Remember to use list comprehensions and to print your results.
print(f"------------------------------------- EJERCICIO 10 -------------------------------------")
path = 'c:/users/ux533f/desktop/ironhack/datamad1020'
files=[f for f in os.listdir(path)]  
print(files) 

#string = os.path.relpath(path, start) 

#11. Create 4 lists of 10 random numbers between 0 and 100 each. Use random_lists as the name of the list. 
#You will probably need to import random module
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 11 -------------------------------------")
random_lists = [random.sample(range(1,101),10) for n in range(4)]
print (random_lists)




#12. Flatten the following list of lists. Use flatten_list as the name of the output.
# Remember to use list comprehensions and to print your results
print(f"------------------------------------- EJERCICIO 12 -------------------------------------")
list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [number for lst in list_of_lists for number in lst]
print(flatten_list)

#13. Convert the numbers of the following nested list to floats. Use floats as the name of the list. 
# Remember to use list comprehensions and to print your results.
print(f"------------------------------------- EJERCICIO 13 -------------------------------------")

list_of_lists = [['40', '20', '10', '30'], ['20', '20', '20', '20', '20', '30', '20'], \
['30', '20', '30', '50', '10', '30', '20', '20', '20'], ['100', '100'], ['100', '100', '100', '100', '100'], \
['100', '100', '100', '100']]

floats = [float(number) for lst in list_of_lists for number in lst] 

print(floats)


#14. Handle the exception thrown by the code below by using try and except blocks. 
print(f"------------------------------------- EJERCICIO 14 -------------------------------------")

for i in ['a','b','c']:
    try:
        print (i**2)
    except Exception as e:
        print ("No se puede elevar un caracter al cuadrado")


#15. Handle the exception thrown by the code below by using try and except blocks. 
#Then use a finally block to print 'All Done.'
# Check in provided resources the type of error you may use. 
print(f"------------------------------------- EJERCICIO 15 -------------------------------------")
x = 5
y = 0

try:
    z = x/y

except ZeroDivisionError:
    print("Are you mad? No dividing by zero")

finally:
    print('All Done')




#16. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print(f"------------------------------------- EJERCICIO 16 -------------------------------------")


try:
    abc=[10,20,20]
    print(abc[3])

except IndexError:
    print("Error: index out of range")







#17. Handle at least two kind of different exceptions when dividing a couple of numbers provided by the user. 
# Hint: take a look on python input function. 
# Check in provided resources the type of error you may use. 
print(f"------------------------------------- EJERCICIO 17 -------------------------------------")

try:
    a = input("Tell me your first number:\n")
    b = input("Tell me your second number:\n")
    print(a/b)

except:
    if ZeroDivisionError:
        print("Error: Cannot divide by zero")

    elif TypeError:
        print("Error: Please enter a number")






#18. Handle the exception thrown by the code below by using try and except blocks. 
# Check in provided resources the type of error you may use. 
print(f"------------------------------------- EJERCICIO 18 -------------------------------------")

try:
    f = open('testfile','r')
    f.write('Test write this')

except FileNotFoundError: 
    print("Error: file not found")




#19. Handle the exceptions that can be thrown by the code below using try and except blocks. 
#Hint: the file could not exist and the data could not be convertable to int
print(f"------------------------------------- EJERCICIO 19 -------------------------------------")

try:
    fp = open('myfile.txt')
        line = f.readline()
        i = int(s.strip())

except IndentationError as e: 
    print e







#20. The following function can only run on a Linux system. 
# The assert in this function will throw an exception if you call it on an operating system other than Linux. 
# Handle this exception using try and except blocks. 
# You will probably need to import sys 
print(f"------------------------------------- EJERCICIO 20 -------------------------------------")



def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')



try:
    linux_interaction()

except AssertionError: 
    print("ERROR: not a Linux system")





# Bonus Questions:

# You will need to make some research on dictionary comprehension to solve the following questions

#21.  Write a function that asks for an integer and prints the square of it. 
# Hint: we need to continually keep checking until we get an integer.
# Use a while loop with a try,except, else block to account for incorrect inputs.
print(f"------------------------------------- EJERCICIO 21 -------------------------------------")
def square():
    while True:
        number = int(input("What number do you want to square?"))
        try:
            return number**2
        except ValueError:
            print("Error: that is not a number")

square()

# 22. Find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9). 
# Use results as the name of the list 
print(f"------------------------------------- EJERCICIO 22 -------------------------------------")
results = [n for n in range(1,1001) for number in range(2,10) if not n%number]



# 23. Define a customised exception to handle not accepted values. 
# You have the following user inputs and the Num_of_sections can not be less than 2.
# Hint: Create a class derived from the pre-defined Exception class in Python

Total_Marks = int(input("Enter Total Marks Scored: ")) 
Num_of_Sections = int(input("Enter Num of Sections: "))

if Num_of_Sections < 2:
    raise Exception ("Sections < 2")

'