''' loops in python - The following loops are available in Python to fulfil the looping needs.
 Python offers 3 choices for running the loops. The basic functionality of all the techniques is the 
 same, although the syntax and the amount of time required for checking the condition differ.
We can run a single statement or set of statements repeatedly using a loop command. 

1. FOR LOOP - Python's for loop is designed to repeatedly execute a code block while iterating through a 
             list, tuple, dictionary, or other iterable objects of Python.The process of traversing a 
             sequence is known as iteration.
syntax :
        for value in sequence:
            code
'''

a=input("enter the string :")
for i in range(1,10):
    print(a)

'''
2. WHILE LOOP - While loops are used in Python to iterate until a specified condition is met. However,
 the statement in the program that follows the while loop is executed once the condition changes to
  false.
syntax :
        while<condiiton> :
            code block
'''
# program to print numbers from one to ten
x=1
while x<=10:
	print(x)
	x+=1



