# print(1,2,3)
print # beware that this is okay but doesn't wor

#######

# import math
#
# # print(math.pi, math.e)
# print(math.sqrt(9))


# from math import e
#
# print(e)

e = 10

print(e)

# from math import e
# from math import *

# print(e)

# make a function called say hello

def say_hello():
    print("hello")
#
# say_hello()
# say_hello()
# say_hello()

# let's add stuff
# def say_hello(name, othername, punc, i): #add an input
#     print("hello", name, "the", othername, punc, i)
#
# say_hello("Leo", "kitten", "!", 2)

# let's add return

def say_hello(name):
    # print(name)
    return "hello " + name

answer = say_hello("Leo")
print(answer)