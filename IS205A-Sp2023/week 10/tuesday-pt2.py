# get acronyms for each line in a file

# read in the file, get access to lines

infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()

# def acry func

def make_acronym(one_line):
    """take a line and return the acronym"""
    acr = ""
    for one_word in one_line.split():
        first_letter = one_word[0]

        if len(one_word) <= 2: # short words
            acr = acr + first_letter
        else: # for longer words
            acr = acr + first_letter.upper()
    return acr

# test case
# print(make_acronym("here is some text"))

# put them together

# print(make_acronym(lines)) # nope, because lines is a list
# we want string input

# for each_line in lines:
#     print(make_acronym(each_line))
# make output, write out the file

outfile = open('threeyearsacr.txt', 'w', encoding='utf-8')

for each_line in lines:
    acr_result = make_acronym(each_line)
    outfile.write(acr_result + "\n")