# decision making statements
'''
1. if statement - The if statement is used to test a particular condition and if the condition is true, 
it executes a block of code known as if-block. The condition of if statement can be any valid logical 
expression which can be either evaluated to true or false.

syntax :
           if expression:
                 #code to be executed
'''
#program to print number is prime or not
a=int(input("enter the integer : "))

if a%2==0:
    print(a,"is a prime number")

'''
2.if-else statement - The if-else statement provides an else block combined with the if statement which 
 is executed in the false case of the condition.
If the condition is true, then the if-block is executed. Otherwise, the else-block is executed.

syntax :
    if expression:
        #code to be executed
    else:
        #code to be executed
'''

# Program to check whether a person is eligible to vote or not.
# Simple Python Program to check whether a person is eligible to vote or not.  
age = int (input("Enter your age: "))    
# Here, we are taking an integer num and taking input dynamically  
if age>=18:    
# Here, we are checking the condition. If the condition is true, we will enter the block  
    print("You are eligible to vote !!");    
else:    
    print("Sorry! you have to wait !!");    

Output:
Enter your age: 90
You are eligible to vote !!

'''
3. elif statement - The elif statement enables us to check multiple conditions and execute the 
specific block of statements depending upon the true condition among them. We can have any number of 
elif statements in our program depending upon our need. However, using elif is optional.
The elif statement works like an if-else-if ladder statement in C. It must be succeeded by an
 if statement.

 syntax :
        if expression 1:
            code
        elif expression 2:
            code
        elif expression 3:
            code
        else:
            code
'''

# program to find out greater number among three numbers

a=int(input("enter first digit:"))
b=int(input("enter second digit:"))
c=int(input("enter third number:"))

if a>b and a>c :
    print(a,"is greater")
elif b>a and b>c :
    print(b,"is greater")
else :
    print(c,"is greater")
        
         