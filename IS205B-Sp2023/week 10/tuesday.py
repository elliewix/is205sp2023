text = "here   is some     text"

print(text.split()) # yes!
# print(text.split(" ")) #NEVER

letter_count = 0
counter = 0
acr = ""
for one_word in text.split():
    # doing business
    print(one_word, len(one_word))
    word_length = len(one_word)
    first_letter = one_word[0]
    # increment stuff
    if word_length <= 2: # short words
        letter_count = letter_count + (word_length * 1.2)
        acr = acr + first_letter.lower() # short gets lowercase
    else: #longer words
        letter_count = letter_count + word_length
        acr = acr + first_letter.upper() # longer gets uppercase
    # acr = acr + first_letter
    counter = counter + 1

print(letter_count)
print(len(text.split()), counter)
print(letter_count / counter, letter_count / len(text.split()))
# print((letter_count * 1.2) / counter)
print(acr)
