#list
print("LISTS: ")
courses = ['history', 'math', 'physics', 'compsci'] #use[]
courses2 = ['art', 'PE']
courses2.extend(courses) #add courses2 then courses
print(courses)
print(courses2)

print() #empty space

for item in courses:
   print(item)

print() #empty space

courses.sort() #abc order
for item in courses:
   print(item) 

print() #empty space

course_str = ' - '.join(courses)
print(course_str) #seperate with ' - '

print() #empty space

courses_1 = ['history', 'math', 'physics', 'compsci']
courses_2 = courses_1

print(courses_1)
print(courses_2)


print() #empty space

courses_1[1] = '_art_'

print(courses_1)
print(courses_2)

print() #empty space







#sets        

cs_courses = {'history', 'math', 'physics', 'compsci', 'math'} #use {}
art_courses ={'history', 'math', 'art', 'design'}

print("SETS: ")
print(cs_courses) #sets remove duplicates... only 1 math on print

print() #empty space

print(cs_courses.intersection(art_courses)) #in both sets

print() #empty space

print(cs_courses.difference(art_courses)) #in cs  not in art

print() #empty space

print(art_courses.difference(cs_courses)) #in art  not in cs

print() #empty space

print(cs_courses.union(art_courses)) #add lists together

print() #empty space






#tuple
print("TUPLES:")
tuple_1 = ('history', 'math', 'physics', 'compsci') #use()
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

print() #empty space

#tuple_1[0] = '_art_' #error cant modify tuple see line 28

print(tuple_1)
print(tuple_2)





#empty list
empty_list = []
empty_list = list()

#empty tuples
empty_tuple = ()
empty_tuple = tuple()

#empty sets
empty_set = {}  #not correct reads as dictionary
empty_set = set()
