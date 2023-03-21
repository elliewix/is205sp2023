# get the acronyms for each line in a file

# open the file, get acces to the lines

infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')
lines = infile.readlines()
infile.close()

# print(lines)

# make the acronym function

def make_acronym(one_line):
    """take in a line and make an acronym from it, return acronym"""
    acr = ""
    for one_word in one_line.split():
        first_letter = one_word[0]
        # acr = acr + first_letter
        if len(one_word) <= 2: # shorter words
            acr = acr + first_letter.lower()
        else: # longer words
            acr = acr + first_letter.upper()
    return acr

# print(make_acronym("here is some text"))

# put them together

for a_line in lines:
    result = make_acronym(a_line)
    # print(result)

# write out the results

outfile = open('threeyearsacr.txt', 'w', encoding='utf-8')

for a_line in lines:
    result = make_acronym(a_line)
    outfile.write(result + "\n")

outfile.close()