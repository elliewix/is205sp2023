text = "banana"

my_list = []

letters = text[2:] # slicing
one_letter = text[0] # indexing

# when indexing.....
# just give one index position, get that one thing back

# index always starts at zero
print("banana"[1])
# print(""[0]) # won't work, empty


# when slicing....
# start, stop, step

print("banana"[0:3]) # give start and stop
print("banana"[:3]) #presumes from beginning
print("banana"[3:]) #presumes to the end
print("banana"[:]) # the whole thing
# start position: inclusive
# stop position: exclusive

# fun tricks

print("banana"[-1])
print("banana"[-2])
print("banana"[-3:]) # "the last three thigns"
print("banana"[-6:3])
print("banana"[-4:-6:-1])
print("banana"[::2])



# step: hops


