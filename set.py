'''
set - A Python set is the collection of the unordered items. 
      Each element in the set must be unique, immutable, and the sets remove the duplicate elements. 
      Sets are mutable which means we can modify it after its creation.
'''
#creation of set using curly braces 
days = {'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
print(days)

#creation using set() method
month = set(['jan','feb','mar','apr','may','jun'])
print(month)

# adding element to set
month.add('jul')
print(month)

# removing items from set
month.discard('may')
print(month)

s1 = {'monday','tuesday','wednesday','saturday'}
s2 = {'monday','friday','sunday','saturday'}

# set union
print(s1|s2)   #using or operator
print(s1.union(s2)) #using union() method

#set intersection
print(s1&s2)  #using & operator
print(s1.intersection(s2))  #using intersection method

#diffrence blw two sets
print(s1 - s2) 

# symmetric difference
c = s1^s2
print(c)

# set comparision
print(s1>s2)
print(s1<s2)
print(s1==s2)

output:
{'monday','tuesday','wednesday','thursday','friday','saturday','sunday'}
{'jan','feb','mar','apr','may','jun'}
{'jan','feb','mar','apr','may','jun','jul'}
{'jan','feb','mar','apr','jun','jul'}
{'monday','tuesday','wednesday','saturday','friday','sunday'}
{'monday','saturday'}
{'tuesday','wednesday'}
{'tuesday','wednesday','friday','sunday'}
false
false
true