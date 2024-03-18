'''list - A list is a collection of different kinds of values or items.
         Since Python lists are mutable, we can change their elements after forming. 
        The comma (,) and the square brackets [enclose the List's items] serve as separators.

The characteristics of the List are as follows:

The lists are in order.
The list element can be accessed via the index.
The mutable type of List is
The rundowns are changeable sorts.
The number of various elements can be stored in a list.
'''

# creaating a list
list1 = [1, 2, "Python", "Program", 15.9]      
list2 = ["Amy", "Ryan", "Henry", "Emma"]   
  
# printing the list  
print(list1)  
print(list2)  
  
# printing the type of list  
print(type(list1))  
print(type(list2)) 

#list indexing
print(list1[2])
print(list2[2:3])

#list updating
list1[2] = ["java"]
print(list1)
list1[0:1] = [2,3]
print(list1)

Output:
[1, 2, 'Python', 'Program', 15.9]
['Amy', 'Ryan', 'Henry', 'Emma']
< class ' list ' >
< class ' list ' >
["python"]
["henry","emma"]
[1,2,"java","program",15.9]
[2, 3, 'Python', 'Program', 15.9]

'''
list operations :
1.Repetition
2.Concatenation
3.Length
4.Iteration
5.Membership
'''
list3=[1,2,3,4,5]
list4=[6,7,8,9,10]

#repetation
a=list1*2
print(a)

#conctenation
b = list3+list4
print(b)

#length of list
len(list1)

#iteration over list
for i in list1:
    print("iteration over list")
    print(list1)

#membership operator
print(3 in list1)
print(7 in list1)

#to add element to list
list1.append(33)
print(list1)

#to add element according to index
list1.insert(2:34)
print(list1)

#to remove element from list
list1.remove(1)
print(list1)

#max function
print(max(list1))

#min function
print(min(list1))


output:
[1,2,3,4,5,1,2,3,4,5]
[1,2,3,4,5,6,7,8,9,10]
iteration over list
1
2
3
4
5
true
false
[1,2,3,4,5,33]
[1,2,34,4,5]
[2,3,4,5]
5
1








