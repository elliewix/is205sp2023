infile = open("Three-years-in-europe.txt", 'r',
              encoding='utf-8')
text = infile.read() # gets the entire thing as a string
infile.close()

# # print(text.split("\n"))
# # print(text)
# for something in text.split("\n"):
#     print("WAT??", something)

infile = open("Three-years-in-europe.txt", 'r',
              encoding='utf-8')
lines = infile.readlines()
infile.close()

# print(lines)

### writing out

outfile = open("linecounts.txt", "w", encoding='utf-8')

for l in lines:
    # charlength = len(l.split())
    # output = str(charlength) + ": " + l # fancy!
    output = str(len(l)) + '\n'
    outfile.write(output)

outfile.close()