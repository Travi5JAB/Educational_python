#functions

def hello_func():
    pass  #no function

print(hello_func)
print(hello_func())  #none no funtion from pass

print() #empty space

def a():
    print("Hello")

a()
a()
a()

print() #empty space

def b():
    return "Hello"

b()   #doesnt print from return
print (b()) #prints
print(b().upper()) #uppercase

print() #empty space

def c(greeting):
    return "{} World!!".format(greeting) #{} insert greeting here

print(c("Hello")) #plug "hello" into greeting

print() #empty space

def d (greeting, name="YOU"):
    return "{},{}!!".format(greeting,name)
print(d("HI"))              #print hi you (you is default)
print(d("HI", name="ME"))   #print hi me

print() #empty space

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)
student_info("math","art",name="John",age=22)

print() #empty space

def student_info2(*args,**kwargs):
    print(args)
    print(kwargs)
courses = ["math","art"]
info = {"name":"John","age":22}

student_info2(*courses,**info)


