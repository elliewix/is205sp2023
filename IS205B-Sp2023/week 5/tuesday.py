# import math #this is the best way
# from math import *
#
# # print(math.e)
# print(e)

#
# x = 10
# e = 5
#
# print(x * e)
# # from math import *
# print(x* e)


####

import math

print(math.sqrt(9))


#####

# getting a start....
# def say_hello():
#     print("hello")
#
# say_hello()

# def say_hello(name):
#     print("hello", name)
#
# say_hello("Leo")

# def say_hello(name, pet):
#     print("hello", name, "the", pet)
#
# say_hello("Leo", "kitten")

# let's do a return statement

def say_hello(name, pet):
    greeting = "hello " + name + " the " + pet
    return greeting

print(say_hello("Leo", "kitten"))
print(say_hello("Elizabeth", "lava cat"))
