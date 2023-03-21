text = "here is   some             text"

# print(text.split())
word_count = 0
char_count = 0
    acr = ""
for one_word in text.split():
    # print(one_word)
    num_chars = len(one_word)
    # char_count = char_count + (num_chars * 1.2)
    if num_chars <= 2:
        char_count = char_count + (num_chars * 1.2)
        # shorter are lowercase
        acr = acr + one_word[0]
    else:
        char_count = char_count + num_chars
        # for the acronym
        letter = one_word[0] # only collect from longer words
        acr = acr + letter.upper()
    word_count = word_count + 1

print(char_count, word_count)
print(char_count/word_count)
# print(len(text.split(" ")))
print(text.split())
# print(text.split(" "))
print(acr)