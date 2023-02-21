phrase = "the cat in here"
#
# for character in phrase:
#     print(character)

# keep java out of your heads
# for i in range(len(phrase)):
#     c = phrase[i]


# # measure something about what your iterable
# phrase = "the cat in here"
#
# for character in phrase:
#     if character == " ":
#         print("XXXXXX")
#     else:
#         print(character)


# do something about it
#string accumulator
phrase = "the cat in here"

new_phrase = "" # step 1, establish base
# outside of and before your for loop
for character in phrase: # step 2, do a loop
    # do stuff, take care of business
    if character == " ":
        # print("XXXXXX") # step 4, identify content
        new_phrase = new_phrase + "XXXXXX" # step 5, collect
        # new_phrase += "XXXXXXX" # eqiv shorthand
    else:
        # print(character)
        new_phrase = new_phrase + character
# print(new_phrase) #6, print the result, outside of and after


######

print(list(range(10)))
# add a counter
# count = 0 # 1
# for i in range(10): # 2, loop
#     # print(i)
#     # print("hello")
#     count = count + 1 # step 5
#     # count += 1 # fine, but advanced
#     # count++ #not in python
#
# print(count)


# add accumulator to this
count = 0 # 1
total = 0
count_error = 0
for i in range(10): # 2, loop
    count = count + 1 # step 5, counter
    total = total + i # step 5, accum
    count_error = count + i # I meant, total = total + i

print(count)
print(total)
print(count_error)