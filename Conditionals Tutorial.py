#IF/ELSE/ELIF

if True:
   print('conditional was true') #prints
if False:
   print('conditional was true') #doesnt print
print() #empty space

language = "python"

if language == 'python':
   print('python') #prints
elif language == 'java':
   print('java')  #print if java
else:
   print('not true')
print() #empty space

user = 'admin'
logged_in = False  #can use 0, [], (), '', {}, or none in place of false
                     #(),[],{} must be empty to be false (run else)

if user == 'admin' and logged_in:   #and means both must be true
   print('admin logged in')
else:
   print('please log in')

print() #empty space


if user == 'admin' or logged_in:   #or means either be true
   print('admin logged in')
else:
   print('please log in')

print() #empty space

a = [1,2,3]
b = [1,2,3]

print(id(a))    #ids dont match
print(id(b))
print(a==b) #true 
print(a is b)#false

print() #empty space

c = [1,2,3]
d = c

print(id(c))    #ids match
print(id(d))
print(c is d)#not its true
