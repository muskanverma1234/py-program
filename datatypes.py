# datatypes - A variable can contain a variety of values. On the other hand, a person's id must be stored as an integer, while their name must be stored as a string.
#The storage method for each of the standard data types that Python provides is specified by Python. The following is a list of the Python-defined data types.

""" types of datatypes in python 
    1.numeric - Numeric values are stored in numbers. The whole number, float, and complex qualities have a place with a Python Numbers datatype. Python offers the type() function to determine a variable's data type. The instance () capability is utilized to check whether an item has a place with a specific class.
    When a number is assigned to a variable, Python generates Number objects.

a = 5  
print("The type of a", type(a))  
  
b = 40.5  
print("The type of b", type(b))  
  
c = 1+3j  
print("The type of c", type(c))  
print(" c is a complex number", isinstance(1+3j,complex))  

Output:
The type of a <class 'int'>
The type of b <class 'float'>
The type of c <class 'complex'>
c is complex number: True
    
a.Int: Whole number worth can be any length, like numbers 10, 2, 29, - 20, - 150, and so on. 
An integer can be any length you want in Python. Its worth has a place with int.
b.Float: Float stores drifting point numbers like 1.9, 9.902, 15.2, etc.
It can be accurate to within 15 decimal place.
c.complex number:An intricate number contains an arranged pair, i.e., x + iy, where x and y signify the genuine and non-existent parts separately.
 The complex numbers like 2.14j, 2.0 + 2.3j, etc. """

 ''' 
 2.sequence type 

a.string - The sequence of characters in the quotation marks can be used to describe the string. 
 A string can be defined in Python using single, double, or triple quotes.
String dealing with Python is a direct undertaking since Python gives 
worked-in capabilities and administrators to perform tasks in the string.

The Python string is demonstrated in the following example.
Example - 1

str = "string using double quotes"  
print(str)  
s = '''''A multiline 
string'''  
print(s)  

Output:
string using double quotes
A multiline
string
'''
'''
b.list - Lists in Python are like arrays in C, but lists can contain data of different types.
 The things put away in the rundown are isolated with a comma (,) and encased inside square sections [].
To gain access to the list's data, we can use slice [:] operators. 
Like how they worked with strings, the list is handled by the concatenation operator (+) and the 
repetition operator (*).

list1  = [1, "hi", "Python", 2]    
#Checking type of given list  
print(type(list1))  
  
#Printing the list1  
print (list1)  
  
# List slicing  
print (list1[3:])  
  
# List slicing  
print (list1[0:2])   
  
# List Concatenation using + operator  
print (list1 + list1)  
  
# List repetation using * operator  
print (list1 * 3)  

Output:
[1, 'hi', 'Python', 2]
[2]
[1, 'hi']
[1, 'hi', 'Python', 2, 1, 'hi', 'Python', 2]
[1, 'hi', 'Python', 2, 1, 'hi', 'Python', 2, 1, 'hi', 'Python', 2]
'''

'''
c.tuple - In many ways, a tuple is like a list. Tuples, like lists, also contain a collection of 
          items from various data types. 
          A parenthetical space () separates the tuple's components from one another.

tup  = ("hi", "Python", 2)    
# Checking type of tup  
print (type(tup))    
  
#Printing the tuple  
print (tup)  
  
# Tuple slicing  
print (tup[1:])    
print (tup[0:1])    
  
# Tuple concatenation using + operator  
print (tup + tup)    
  
# Tuple repatation using * operator  
print (tup * 3)     
  
# Adding value to tup. It will throw an error.  
t[2] = "hi"  
Output:

<class 'tuple'>
('hi', 'Python', 2)
('Python', 2)
('hi',)
('hi', 'Python', 2, 'hi', 'Python', 2)
('hi', 'Python', 2, 'hi', 'Python', 2, 'hi', 'Python', 2)

Traceback (most recent call last):
  File "main.py", line 14, in <module>
    t[2] = "hi";
TypeError: 'tuple' object does not support item assignment
'''

'''
3.dictionary - A dictionary is a key-value pair set arranged in any order.
 It stores a specific value for each key, like an associative array or a hash table.
  Value is any Python object, while the key can hold any primitive data type.
The comma (,) and the curly braces are used to separate the items in the dictionary.

Look at the following example.

d = {1:'Jimmy', 2:'Alex', 3:'john', 4:'mike'}     
  
# Printing dictionary  
print (d)  
  
# Accesing value using keys  
print("1st name is "+d[1])   
print("2nd name is "+ d[4])    
  
print (d.keys())    
print (d.values())    
Output:

1st name is Jimmy
2nd name is mike
{1: 'Jimmy', 2: 'Alex', 3: 'john', 4: 'mike'}
dict_keys([1, 2, 3, 4])
dict_values(['Jimmy', 'Alex', 'john', 'mike'])
'''

'''
4.boolean - True and False are the two default values for the Boolean type. 
These qualities are utilized to decide the given assertion valid or misleading. 
The class book indicates this. False can be represented by the 0 or the letter "F," while true 
can be represented by any value that is not zero.

Look at the following example.

# Python program to check the boolean type  
print(type(True))  
print(type(False))  
print(false)  
Output:

<class 'bool'>
<class 'bool'>
NameError: name 'false' is not defined
'''

'''
5.set - the data type's unordered collection is Python Set.
 It is iterable, mutable(can change after creation), and has remarkable components. 
 The elements of a set have no set order; It might return the element's altered sequence. 
 Either a sequence of elements is passed through the curly braces and separated by a comma to create 
 the set or the built-in function set() is used to create the set. It can contain different kinds of
  values.

Look at the following example.

# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)  
Output:

{3, 'Python', 'James', 2}
{'Python', 'James', 3, 2, 10}
{'Python', 'James', 3, 10}

'''