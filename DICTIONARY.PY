'''
dictionary - Dictionaries are a useful data structure for storing data in Python because they are 
         capable of imitating real-world data arrangements where a certain value exists for a given key.

The data is stored as key-value pairs using a Python dictionary.
>> This data structure is mutable
>> The components of dictionary were made using keys and values.
>> Keys must only have one component.
>> Values can be of any type, including integer, list, and tuple.
A dictionary is, in other words, a group of key-value pairs, where the values can be any Python object.
 The keys, in contrast, are immutable Python objects, such as strings, tuples, or numbers.
 '''

 # creating dictionary
 Employee = {"Name": "Johnny", "Age": 32, "salary":26000,"Company":"^TCS"}        
print(type(Employee))        
print("printing Employee data .... ")        
print(Employee)

# fetching data from dict.
print("Name : %s" %Employee["Name"])      
print("Age : %d" %Employee["Age"])   

#adding data to dictionary
var2=['johnny lewer']
print(type(var2))
Employee.update({'full_name': var2})
print(Employee)

#deleting element
pop_key = Employee.pop('name')
print(Employee)

#iterating dictionary
for i in Employee:
    print(i)

output :
<class 'dict'>
printing Employee data .... 
{'Name': 'Johnny', 'Age': 32, 'salary': 26000, 'Company': TCS}
name : Johnny
age : 32
{'Name': 'Johnny', 'Age': 32, 'salary': 26000, 'Company': TCS,'full_name':'johnny lewer'}
{ 'Age': 32, 'salary': 26000, 'Company': TCS,'full_name':'johnny lewer'}
Name
Age
salary
Company
