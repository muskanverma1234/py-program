'''
Loop Control Statements
Statements used to control loops and change the course of iteration are called control statements.
 All the objects produced within the local scope of the loop are deleted when execution is completed.
Python provides the following control statements. We will discuss them later in detail.

Let us quickly go over the definitions of these loop control statements.

1	Break statement : This command terminates the loop's execution and transfers the program's control 
    to the statement next to the loop.
2	Continue statement : This command skips the current iteration of the loop. The statements following 
     the continue statement are not executed once the Python interpreter reaches the continue statement.
3	Pass statement : The pass statement is used when a statement is syntactically necessary, but no code
     is to be executed.
'''

# break statement example  
my_list = [1, 2, 3, 4]  
count = 1  
for item in my_list:  
    if item == 4:  
        print("Item matched")  
        count += 1  
        break  
print("Found at location", count)  
Output:
Item matched
Found at location 2

# Python code to show example of continue statement  
# looping from 10 to 20  
for iterator in range(10, 21):  
   
    # If iterator is equals to 15, loop will continue to the next iteration  
    if iterator == 15:  
        continue  
    # otherwise printing the value of iterator  
    print( iterator )  
Output:
10
11
12
13
14
16
17
18
19
20

# Python program to show how to use a pass statement in a for loop  
'''''pass acts as a placeholder. We can fill this place later on'''  
sequence = {"Python", "Pass", "Statement", "Placeholder"}  
for value in sequence:  
    if value == "Pass":  
        pass # leaving an empty if block using the pass keyword  
    else:  
        print("Not reached pass keyword: ", value)  
Output:
Not reached pass keyword:  Python
Not reached pass keyword:  Placeholder
Not reached pass keyword:  Statement