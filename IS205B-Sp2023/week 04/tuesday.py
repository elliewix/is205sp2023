x = 5

# print(x > 0)
# print(x < 10)

x = -5
greaterthan = x > 0
lessthan = x < 10
# print(greaterthan, lessthan)
# print(greaterthan and lessthan)
# print(greaterthan or lessthan)

x = -5

# if x > 0:
#     print("not negative")
# else:
#     print("negative")

x = 500
#
# if x > 0:
#     print("not negative")
# elif x < 10:
#     print("less than ten")
# else:
#     print("this should never run")

x = 5

greaterthan = x > 0
lessthan = x < 10

# if (x > 0) and (x < 10):
# if greaterthan and lessthan:
# if (greaterthan == True) and (lessthan == True):
#     print("both!")
# else:
#     print("not both?")


# x = 50
# greaterthan = x > 0
# lessthan = x < 10
#
# if greaterthan == True:
#     print('positive!')
# elif lessthan == True:
#     print("less than 10")
# else:
#     print('neither?')

x = 50
greaterthan = x > 0
lessthan = x < 10

if greaterthan == True:
    if lessthan == True:
        print("both!")
    else:
        print("positive, but too big")
else:
    print("neither")