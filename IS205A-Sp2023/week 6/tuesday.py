# phrase = "cat is here"
#
# # isolate and measure
# for character in phrase:
#     if character == " " or character == "e":
#         print("XXXXXXX")
#     else:
#         print(character

# keey java out of your head
# for i in range(len(phrase)):
#     # stuff


phrase = "cat is here with dog"
new_phrase = ""
# collecting it up
for character in phrase:
    if character == " " or character == "e":
        # print("XXXXXXX")
        new_phrase = new_phrase + "XXXXXXX"
        # new_phrase = "XXXXXXX" + new_phrase
        # order matters for strings
    else:
        # print(character)
        new_phrase = new_phrase + character

    # print(new_phrase) #compare the result here vs outside
# print(new_phrase)

####

# use range to generate some numbers
# print(list(range(10)))

for i in range(10):
    print(i) # sometimes we want the numberr
    # print("hello") # sometimes not