#for loop
nums = [1,2,3,4,5]

print(nums)
print() #empty space

for num in nums:
   if num == 3:
      print("found")
      break     #stop at 3
   print(num)

print() #empty space

for num in nums:
   if num == 3:
      print("found")
      continue    #continue after 3
   print(num)

print() #empty space

for num in nums:
   for letter in 'abc': #all combinations on nums and letters a,b and c
      print(num, letter)

print() #empty space

#while loop

x = 0
while x <10:
   print(x)
   x += 1 #add one to x

print() #empty space

y = 0
while True: #infinate loop condition cant be met
   if y == 5: 
      break   #stops at 5
   print(y)
   y += 1 
