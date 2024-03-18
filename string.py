# python string 
''' 
Python string is the collection of the characters surrounded by single quotes, double quotes, or triple 
quotes. The computer does not understand the characters; internally, it stores manipulated character as 
the combination of the 0's and 1's.
Each character is encoded in the ASCII or Unicode character. So we can say that Python strings are also 
called the collection of Unicode characters.
'''

str="hello world" #creating a string
print(str)
print(type(str))  #shows string type
print(str[3])  # string indexing
print(str[7])
print(str[1:4]) #string slicing
print(str[::-1]) #reverse the given string

output: hello world
        <class type str>
        l
        w
        ello
        dlrow olleh

''' String Operators

+ - It is known as concatenation operator used to join the strings given either side of the operator.
* - It is known as repetition operator. It concatenates the multiple copies of the same string.
[] - It is known as slice operator. It is used to access the sub-strings of a particular string.
[:] - It is known as range slice operator. It is used to access the characters from the specified range.
in - It is known as membership operator. It returns if a particular sub-string is present in the specified string.
not in - It is also a membership operator and does the exact reverse of in. It returns true if a particular substring is not present in the specified string.
r/R	- It is used to specify the raw string. Raw strings are used in the cases where we need to print the actual meaning of escape characters such as "C://python". To define any string as a raw string, the character r or R is followed by the string.
% - It is used to perform string formatting. It makes use of the format specifiers used in C programming like %d or %f to map their values in python. We will discuss how formatting is done in python.
Example
Consider the following example to understand the real use of Python operators.
'''

str = "Hello"     
str1 = " world"    
print(str*3) # prints HelloHelloHello    
print(str+str1)# prints Hello world     
print(str[4]) # prints o                
print(str[2:4]); # prints ll                    
print('w' in str) # prints false as w is not present in str    
print('wo' not in str1) # prints false as wo is present in str1.     
print(r'C://python37') # prints C://python37 as it is written    
print("The string str : %s"%(str)) # prints The string str : Hello     

Output: HelloHelloHello
        helloworld\
        o
        ll
        False
        False
        C://python37
        The string str : Hello
 




