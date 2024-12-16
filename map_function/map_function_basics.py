# # use of map ()
# # it is a function that applies a given function to all items in an input list(iterators)
# # and return a map object (iterator) of the result
#
# # syntax:
#
# # map (function,iterator1,iterator2,...)
#
# def square (x):
#     return x*x
#
# numbers = [1,2,3,4,5]
# square = list(map(square,numbers))
# print(square)   #output=[1,4,9,16,25]
#
# # another method with the use of lambda function
#
# square = list(map(lambda x : x*x,numbers))
# print(square)   #output=[1,4,9,16,25]
#
# # map function with multiple iterables and when the length of the iterable object the same
#
# number1 = [2,3,4,6,1]
# number2 = [9,5,4,3,0]
#
# add_numbers = list(map(lambda x,y:x+y,number1,number2))
# print(add_numbers)   #output=[11,8,8,9,1]
#
# # when the length of the iterable object different
# # if this so , the mapping stops when the shortest iterator exhausted
# num1 = [1,2,3,4]
# num2 = [5,3,4,6,7,3,7]
#
# addition = list(map(lambda x,y:x+y,num1,num2))
# print(addition) #output = [6,5,7,10]
#
# # to handle different length we can import zip_longest from itertools
# # zip_longest() fills in missing values with specific fill in value,
# # by this it helps to handle different length iterables
# #
# from itertools import zip_longest
#
# num1 = [1,2,3,4]
# num2 = [5,3,4,6,7,3,7]
# result = list(zip_longest(num1,num2)) # it forms tuple from take each nums
# print(result)   #output = [(1,5),(2,3),(3,4),(4,6),(None,7),(None,3),(None,7)]
# addition_num = list(map(lambda z:(z[0] or 0) + (z[1] or 0),result))
# print(addition_num)  # the use of 0 is to replace the vale of 'None'
#            # output = [6, 5, 7, 10, 7, 3, 7]
#
# # map () combined with enumerate()
# # it is useful when you need to apply function to each elements of an iterable
# # while keeping track of the index
#
# numbers = [10,23,45,32]
# result = list(map(lambda z:z[0]+z[1],enumerate(numbers)))
# print(result) #output = [10,24,47,35]
#
# # or other method by defining a function
# # def sum_index_num(number,index):
# #     return number + index
# # result = list(map(lambda x: sum_index_num(x[0],x[1]),enumerate(numbers)))
# # print(result)
#
# # map ()  combined with zip ()
# # we use this combination, when we want to apply a function to a pairs
# # or groups of elements of from multiple iterables
# list1 = [9,3,4,5,6,7]
# list2 = [8,5,3,4,6]
#
# #to get the sum of each index corresponding elements of each iterators
# result = list(map(lambda x:x[0]+x[1], zip(list1,list2)))
# print(result) #output = [17,8,7,9,12]

# map() combined with both enumerate () and zip()
# it use for example , you have two lists and want to
# add corresponding elements along with their indices
list1 = [9,3,4,5,6,7]
list2 = [8,5,3,4,6]
def sum_index (index,x,y):
    return index+x+y
result = list(map(lambda x:sum_index(x[0],x[1][0],x[1][1]),enumerate(zip(list1,list2))))

print(result)





