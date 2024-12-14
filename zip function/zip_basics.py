# zip is python built in function
#zip allow us to combine multiple iterables (lists,tuples, strings)
# into a single iterabel of tuples
# the first tuples contains the first elements of each iterable and secon and so on.
# if the input iterables are of different lengths,
# zip() stop creating tuples when the shortest input iterable is exhausted

# syntax:  zip(*iterables) : -->*iterables(many iterables as much as we want)



# zip () with the same length iterable inputs

list1=[1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']
zipped = zip(list1,list2)
print(type(zipped))   #output = <'class' zip>
print(list(zipped))  #output=[(1,'a'),(2,'b'),(3,'c'),(4,'d')]

# zip() with different length iterable inputs

list1 = [1, 2, 3]
list2 = ['y','i']
zipped = zip(list1,list2) # creation of tuple continue till 'i'
print(list(zipped))    #output=[(1,'y'),(2,'i')]


# zip() with multiple iterables

name = ['yibeltal','temesgen','mayi','abaynew','john']
sex = ['M', 'M', 'F', 'M', 'M']
grade = ['A','A+','B','A-','A']

combiled_zip = zip(name, sex, grade)

print(list(combiled_zip))  #output=[('yibeltal','M','A'),('temesgen',M','A+')..]


# unzipping the zip tuple using zip itself

zipped_file = [(1,'a','social'),(2,'b','cs'),(29,'y','soft'),(83,'t','all')]
unzipped_file = zip(*zipped_file)
list1,list2,list3 = list(unzipped_file)
print(list1)  #output = (1,2,29,83)
print(list2)  #output = ('a','b','y','t')
print(list3)  #output = ('social','cs','soft','all')


zipped = [(1,'yibeltal'),(2,"abaynew"),(3,"yared")]

unzipped = zip(*zipped)

number, name = list(unzipped)

print(number) #output = (1, 2, 3)
print(name)   #output = ('yibeltal', 'abaynew', 'yared')

# application of this zip function

name = ['name','age','department']
information = ['yibeltal',22,'software']

zipped = zip(name,information)

dictionary = dict(zipped)  # or dict(zip(name, information)
print(dictionary) #{'name':'yibeltal','age':22,'department':'software'}