#example one
age=60
if age>18:
 print("you are an aduli")
elif age>65:
 print("you are a senior citizen")
else:
 print("you are a youth")

#example two
grade=45
if grade>=90:
 print("Excellent")
elif age>13 and age<18:
 print("discount for price = shs 500")
elif grade>=80:
 print("Very good")
elif grade>=70:
 print("Good")
else:
 print("Not good")

# exerise one
age=18
if age<13:
 print("price = shs1000")
elif age>13 and age<18:
 print("discount for price = shs 500")
elif age<=18 and age>=65:
 print("pay full price of shs 2000")
else:
 print("senior citizen pay full price of shs 5000")

#  loops
#  for loops(lists,tuples,dictionary,set,string)
#  while repears as long as yhe condition is true

#example three
cars=["Telsa","BMW","Audi","Jeep","RangeRover"]
for car in cars:
 print(car)

#example four
count=1
while count<=10:
 print("count 1 to 10:", count)
 count += 1
 colors=["blue","purple","red","green"]
 reverse=colors[::-1]
for color in colors:
 print(color) 
 #reversing a list
 for color in reverse:
  print(color)

 list=[1,2,3,4,5]
 index=len(list)-1
 while index>0:
  print(list[index])
  index -=1
