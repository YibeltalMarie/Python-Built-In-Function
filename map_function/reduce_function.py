# it;s a part of functools , so we need to import it first

#reduce() applies a specific function (that takes two arguments)
# to the items of iterables,from left to right, to reduce to a single value

#syntax
# from functools import reduce
# reduce (function,iterable,initializer)
#'initializer':a value to start the accumulation. if it's specified the function is first
# called with the initializer and first item from the iterable.
# but if it's not specified the function is first called with two items from the iterable
# and by default takes the first element as the initializer

# reduce () without initializer

from functools import reduce

numbers = [1,2,3,4,5]
def add(x,y):
    return x+y
result = reduce(add,numbers)
print(result) #output = 15

# reduce () with initializer

result = reduce(lambda x,y:x+y,numbers,10)  # initial = 10
print(result)    # output = 25
                 # first x = 10 , y=1
                 # second x = 11 , y = 2 , so on

# to get the product of the each elements of the iterable

result = reduce(lambda x,y: x*y,numbers)
print(result)  #output = 120

# to flatten the list or to combine the nested list to a single list
lists = [[1,2,3],[4,5,6],[7,8,9]]

result = reduce(lambda x,y:x+y,lists)
print(result)  # output = [1, 2, 3, 4, 5, 6, 7, 8, 9]
               # first x = [1,2,3],y=[4,5,6] ,lambda return x+y [1,2,3,4,5,6]
               # second x = [1,2,3,4,5,6] , y = [7,8,9] return x+y [1,2,3,4,5,6,7,8,9]

# to find the greatest common divisor
import math

numbers = [48,120,244]
print(math.gcd(48,120))  # 24
print(math.gcd(24,244)) # 4
GCD = reduce(math.gcd,numbers)
print(GCD)  #output = 4
        # first x=48,y=120 , fun:math.gcd(24,120) = 24(this becomes the new x for the 2nd)
        # second x = 24,y=244 , fun: math.gcd(24,244) = 4

# we can use map() to preprocess the data before reducing it
lists = [6,7,3,4,8]
squared_numbers = map(lambda x:x*x,lists)
result = reduce(lambda x,y:x*y, squared_numbers)
print(result)

# we can use filter() to remove the unwanted element before apply reduce()
even_numbers = list(filter(lambda x:x%2==0,lists))
print(f"even numbers from the {lists} :",even_numbers)  #output =
sum_of_even_numbers = reduce(lambda x,y:x+y,even_numbers)
print(f"sum of even numbers from the {lists}:",sum_of_even_numbers)

# reduce () with enumerate ()
from functools import reduce
numbers = [2,3,4,5,6,7]
result = reduce(lambda acc,pair:acc+pair[0]*pair[1],enumerate(numbers),0)

print(result)

# we can use list comprehension to preprocess the date before the reduce ()
square_even_numbers = [x*x for x in numbers if x%2==0]
print(square_even_numbers)  # output = [4,16,36]
sum_even_number = reduce(lambda x,y:x*y,square_even_numbers)
print(sum_even_number)  # output = 2304


