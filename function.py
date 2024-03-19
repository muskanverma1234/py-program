'''
Function - A collection of related assertions that carry out a mathematical, analytical, or evaluative
           operation is known as a function. 
advantages of function :
1. Once defined, Python functions can be called multiple times and from any location in a program.
2.Our Python program can be broken up into numerous, easy-to-follow functions if it is significant.
3.The ability to return as many outputs as we want using a variety of arguments is one of Python's most
 significant achievements.
4.However, Python programs have always incurred overhead when calling functions.

syntax:
def function_name(parameters):
    code block
'''

#creating function 
def square():
    return num**2
s1=square(6)
print("square of given number is",s1)

output : square of given number is 36

'''
two types of functions :
1.built-in functions : The Python built-in functions are defined as the functions whose functionality 
                       is pre-defined in Python. The python interpreter has several functions that are
                        always present for use. These functions are known as Built-in Functions. 
                        There are several built-in functions in Python which are listed below:

float() -it returns the floating point number form a number or string.
print(float(9)) --> 0.9

sum() - used to get the sum of numbers of an iterable i,e. list
p=sum([1,4,5])
print(p) --> 10

len() - the length function is used to return the length of an object.
str = "muskan"
print(len(str)) --> 6

min() - it is used to find out the smallest number from the given collection.
m = [2,5,8]
print(min(m)) --> 2

pow() - it is used to calculate the power of given number.
print(pow(2,3)) --> 8



