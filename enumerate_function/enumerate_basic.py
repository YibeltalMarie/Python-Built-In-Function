#syntax of enumerate funtion
# enumerate(iterables,start=_) __>iterables=list,tuples,strings  start=tells it from where the index start
# so it returns the index first and the value of each elements of the iterable
from tkinter.font import names

name_lists= ['yibeltal','temesgen','abaynew']

for index,name in enumerate(name_lists):
    print(index,name)

# when we use start in this function to specify from where the index start and with tuple

fruits = ('apples','mango','banana',)
for index, fruit in enumerate(fruits , start=1):
    print(index,fruit)

colors = ('red','green','blue','yellow')
for index, color in enumerate(colors, start=3):# start by 3 red
    print(index,color)
# enumerate with strings

alphabet = "YIBELTALMARIE"
for index , letter in enumerate(alphabet, start=1):
    print(index,letter)

# when enumerate function combine with zip function

names = ["yibelal","temesgen","abayney"]
ages = [21,24,22]

for index, (name, age) in enumerate (zip(names,ages),start=1): # name and age need to be inside the tuple to access them
    print(f"{index}:{name} is {age} years old")

# when enumerate function combine with list Comprehension

indexed_name = [(index, name) for index, name in enumerate(names,start=1)]

print (indexed_name)

# it combine with reversed function to reverse the iterables(eg. below to reverse indexed_name)

for index1,(index2,name) in enumerate (reversed(indexed_name)):
    print(f"{index1}:({index2},{name})")

