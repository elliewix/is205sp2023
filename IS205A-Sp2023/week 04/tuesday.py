x = 5

# greaterthan = x > 0
# lessthan = x < 10
# print(greaterthan, lessthan)
# print(greaterthan and lessthan)

price = -2
greaterthan = price >= 0
lessthan = price <= 10

# if greaterthan == True:
#     print("at least not negative?")
# elif lessthan == True:
#     print("not too high! ")
# else:
#     print("negative price")

price = 2
greaterthan = price >= 0
lessthan = price <= 10

# if greaterthan and lessthan:
# if (price >= 0) and (price <= 10):
#     print("not negative and less than 10!")
# else:
#     print("can't do it for soem reason")
#

price = -20
greaterthan = price >= 0
lessthan = price <= 10

if greaterthan == True:
    print("more than zero?")
    if lessthan == True:
        print("less than 10!")
else:
    print("nope")