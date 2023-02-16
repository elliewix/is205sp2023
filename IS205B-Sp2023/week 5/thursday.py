def repeat_word(word, repeats):
    # result = "???" # step 3?
    result = word * repeats
    return result

print(repeat_word("cats", 3))
for i in range(5):
    print(i, repeat_word("hello", i))