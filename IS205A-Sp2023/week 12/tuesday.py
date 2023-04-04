# dictionaries

# expect keys to be strings
# value data types matter less
# for both: they should internally match

fruit = {'apples': 10, 'bananas': 5}

# getting stuff out

apples = 20

# ask for key by name, needs to match!
# print(fruit['apples']) #yes, literal match
# print(fruit[apples])# can't do this!
key_to_find = 'apples'
print(fruit[key_to_find]) # you can use variables
# but the content needs to be correct

# useful methods for getting stuff out...

print(list(fruit.keys())) # get a list of keys
print(list(fruit.values())) # get a list of values

# great way to loop
for k in fruit.keys(): # don't need to recast here
    print(k, fruit[k])
# even better if you're comfy with it
for key, value in fruit.items():
    print(key, value)


# populating a dictionary

## changing a value

fruit['bananas'] = 15 # will update
fruit['oranges'] = 25 # will add a new pair
print(fruit)

## they're the same syntax!

# programmatically populating a dict

d = {} # dict()

veggies = ['carrot', 'tomato', 'beans']
## prepopulate
for veg in veggies:
    d[veg] = 0
print(d)

data = "ctbcccbbbbbttccccbbb"
for item in data:
    if item == "c":
        d['carrot'] = d['carrot'] + 1
    elif item == 't':
        d['tomato'] = d['tomato'] + 1
    elif item == 'b':
        d['beans'] += 1 # shorthand, use if comfy

print(d)

d_v2 = {}

for item in data:
    if item in d_v2: # will check if item is a key
        d_v2[item] += 1
    else: # not an existing key
        # establish value, using 1 because you've seen one
        d_v2[item] = 1 # use assignment notation

print(d_v2)

letters = "aoeuidhtnsaeutiaeridaoeuaoeuaoeuaoeuaoeu"
unique_letters = set(letters)
letter_counts = {}
for letter in unique_letters:
    # make each letter a key and each value as 0
    letter_counts[letter] = 0
print(letter_counts)
# now populate
for l in letters:
    #because I've prepopulated, I don't need to check
    letter_counts[l] = letter_counts[l] + 1
    # letter_counts[l] += 1 # the shorthand, same thing
print(letter_counts)

letter_collections = {}

for l in letters:
    # check if it's there
    if l in letter_collections:
        # increment
        letter_collections[l].append(l)
    else:
        # establish
        letter_collections[l] = [l]
print(letter_collections)


