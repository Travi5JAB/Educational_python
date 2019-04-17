#DICTIONARYS
student = {'name':'Jon', 'age': 25, 'courses':['math', 'science']}

print(student)
print() #empty space

print(student.get('name'))
print() #empty space

print(student.get('phone','Not Found')) #return not found when phone is not in student variable
print() #empty space

age = student.pop('age') #remove age from dict
print(student)
print(age)
print() #empty space

student.update({'name':'jane', 'age':26, 'phone': '555-666-7777'})

print(student)
print(student.get('phone','Not Found'))  #phone prints from update
print() #empty space

print(len(student)) # num of variables (after update)
print() #empty space
print(student.keys()) # keys only
print() #empty space

print(student.values())  #values only
print() #empty space

print(student.items())  #keys and values grouped
print() #empty space

for key in student:
   print(key)   #vertical list keys only
print() #empty space

for key, value in student.items():
   print(key,":",value)   #vertical list keys and values
