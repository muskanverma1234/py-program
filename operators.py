''' 
    operators - operators are used to perform operation on two operands .
    for example - a+b , here a and b are two operands and + is an operator.

    types of operators :

    1.arithmetic operators - they are used to perfrom arithmetic operation on operands.
    (+,-,*,/,%,**,//)

    2.assignment operators - they are used to assign values to the variables.
    (=,+=,-=,*=,/=,%=,**=,//=)

    3.comparision operator - they are used to compare value of two operands.
    (==,!=,<=,>=,<,>)

    4.bitwise operator - two operands value are processed bit by bit by this operator.
    (&,\,^,~,<<,>>)

    5.logical operator - the assessment of expression to make decision.
    (AND,OR,NOT)

    6.membership operator - the membership of a value inside a python data structure can be verified
                         using python membership operator.
    (in,not in)

    7.identity operator - they are used to check that the item exist or not.
    (is , is not)
'''

#arithmetic operator
a=10
b=5
print("addition is:",a+b)
print("substraction is:",a-b)
print("multiplication is:",a*b)
print("division is:",a/b)
print(" reminderis:",a%b)
print("exponent is:",a**b)
print("float value is:",a//b)

#assignment operator
print("a==b",a==b)
print("a+=b",a+b)
print("a-=b",a-b)
print("a*=b",a*b)
print("a/b",a/b)
print("a**b",a**b)
print("a//b",a//b)

#comparision operator
print("two numbers are equal or not",a==b)
print("two numbers are not equal or not",a!=b)
print("a is less then or equal to b",a<=b)
print("a is greater than or equal to b",a>=b)
print("a is greater than b",a>b)
print("a is less than b",a<b)

#bitwise operator
print("a&b",a&b)
print("a\b",a\b)
print("a^b",a^b)
print("~a",~a)
print("a<<b",a<<b)
print("a>>b",a>>b)

#logical operator
print("is this statement true",a>3 and a<5)
print("any one statement is true",a>3 or a<5)
print("each statement is true then return false and vice-versa",(not(a>3 and a<5)))

#membership operator
x=["rose","lotus"]
print("is value present in x", "rose" in x)
print("is value not present in x","rupal" not in x)

#identity operator
s=["rose","lotus"]
r=["rose","lotus"]
p=s
print(a is p)
print(a is not p)
print(a is b)
print(a is not b)
print(a==b)
print(a!=b)












