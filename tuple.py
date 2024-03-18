# TUPLES 
'''
A comma-separated group of items is called a Python triple. The ordering, settled items, and 
reiterations of a tuple are to some degree like those of a rundown, but in contrast to a rundown, 
a tuple is unchanging.
'''
'''
Features of Python Tuple
Tuples are an immutable data type, meaning their elements cannot be changed after they are generated.
Each element in a tuple has a specific order that will never change because tuples are ordered 
sequences.
'''

#tuple creation
tup1 = (1,2,3,4)
print(tup1)

#tuple indexing
print(tup1[3])

#tuple slicing
print(tup1[1:3])

#tuple repetation
tup1 = tup1 * 3
print(tup1)

#tuple count()
tupl = tup1.count(2)
print(tupl)

# membership operator
print(2 in tup1)
print(6 in tup1)

# iterating over tuple
t1 = ("python","tuple","ordered","immutable")
for i in t1:
    print(i)
    
output : 
(1,2,3,4)
(4)
(2,3,4)
(1,2,3,4,1,2,3,4,1,2,3,4)
1
true
false
