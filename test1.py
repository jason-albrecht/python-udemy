import math
# Numbers: either ints or floats

# Strings: series of text characters

#

# Numbers

p1 = 100.25 - 12 + 4 ** 2 / 3 * 7

print(p1)

p2 = 4 * (6 + 5)

print(p2)

p3 = 4 * 6 + 5

print(p3)

p4 = 4 + 6 * 5

print(p4)

# type of expression

# decimal

p5 = math.sqrt(p4)

print(p5)

#TODO get answer
# how to get square

s = 'hello'

print(s[1])

print(s[::-1])

print(s[-1])
print(s[4])

list = [0,0,0]
print(list)
list_2 = [0] * 3
print(list_2)
# list.


list3 = [1,2,[3,4,'hello']]

list3[2][2] = 'goodbye'

print(list3)

#TODO get answer
# list4 = [5,3,4,6,1]
# list4_sort = list4.sort()
# print(list4_sort)

d = {'simple_key':'hello'}
val = d['simple_key']
print(val)
d2 = {'k1':{'k2':'hello'}}
val2 = d2['k1']['k2']
print(val2)

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
val3 = d3['k1'][0]['nest_key'][1][0]
print(val3)

d4 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
val4 = d4['k1'][2]['k2'][1]['tough'][2][0]
print(val4)

# can you sort a dictionary?

    # no, it is a map and not a sequence

# diff between list and tuples?
    #tuples are immutable

#how do you create a tuple
    # put items in parentheses

# set shows the unique values

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))