''' comments - Our code is more comprehensible when we use comments in it. It assists us in recalling why specific sections of
             code were created by making the program more understandable.

Below are some of the most common uses for comments:
1.Readability of the Code
2.Restrict code execution
3.Provide an overview of the program or project metadata
4.To add resources to the code

Types of Comments in Python

1.Single-Line Comments
Single-line remarks in Python have shown to be effective for providing quick descriptions for parameters
, function definitions, and expressions. A single-line comment of Python is the one that has a hashtag #
 at the beginning of it and continues until the finish of the line.
'''
Code
# This code is to show an example of a single-line comment  
print( 'This statement does not have a hashtag before it' )  
Output:
This statement does not have a hashtag before it

'''
2.Multi-Line Comments
Python does not provide the facility for multi-line comments. However, there are indeed many ways to create multi-line comments.

With Multiple Hashtags (#)

In Python, we may use hashtags (#) multiple times to construct multiple lines of comments. Every line with a (#) before it will be regarded as a single-line comment.

Code
# it is a  
# comment  
# extending to multiple lines  
'''
''' 
3.Python Docstring
The strings enclosed in triple quotes that come immediately after the defined function are called Python 
docstring. It's designed to link documentation developed for Python modules, methods, classes, and 
functions together. It's placed just beneath the function, module, or class to explain what they
 perform. The docstring is then readily accessible in Python using the __doc__ attribute.

Code

# Code to show how we use docstrings in Python  
  
def add(x, y):  
    """This function adds the values of x and y"""  
    return x + y  
   
# Displaying the docstring of the add function  
print( add.__doc__ ) 

Output:
This function adds the values of x and y
'''
