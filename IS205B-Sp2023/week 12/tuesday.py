#d = {'key': 'value'}
# empty:
#d = {} # or dict()

fruit = {'apples': 10, 'bananas': 5}
# get a value out
# use the key, must match!
# print(fruit['apples']) #yes!
# apples = 25
# print(fruit[apples]) # nope!
f = 'apples'
print(fruit[f]) # very common!

# changing a value

fruit['apples'] = 25
print(fruit)
# adding a new pair
fruit['pear'] = 23
print(fruit)

## extraction methods for dicts

print(list(fruit.keys()))
print(list(fruit.values()))

# looping over dicts to get values

for key in fruit.keys(): # don't need to recast here
    print(key, fruit[key])

# a nicer version, if you like it

for key, value in fruit.items():
    print(key, value)

## programmatically populating a dict


data = {}
# veggies = ['carrots', 'beans', 'tomato']
observations = "ccccttbbbbcctctctbbbpppppp"

# veggies = ['c', 'b', 't']
veggies = set(observations)
for veg in veggies: # prepop with 0
    # print(veg) # always check!!
    data[veg] = 0
# print(data)

for ob in observations:
    data[ob] = data[ob] + 1
    # data[ob] += 1 # same thing,shorthand

print(data)

# dict accumulator, but all at once

data_v2 = {}

for ob in observations:
    if ob in data_v2: # does this key already exist
        data_v2[ob] = data_v2[ob] + 1 # increment
    else: #not in the dict
        data_v2[ob] = 1

print(data_v2)

print(data_v2['c'])

for key in data_v2.keys():
    value = data_v2[key]
    print(key, value)