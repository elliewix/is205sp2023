infile = open("Three-years-in-europe.txt", "r",
              encoding="utf-8")
text = infile.read()
infile.close()

# print(text)
# for something in text:
#     print(something)

# for c in text:
#     print(c)


# what if I wanted lines?

lines = text.split('\n')
# print(lines)

#####

infile = open("Three-years-in-europe.txt", "r",
              encoding="utf-8")
lines = infile.readlines()
infile.close()

# print(lines)
######

outfile = open("linecounts.txt", "w", encoding='utf-8')
# outfile.write("here's some text!")
for l in lines:
    wordcount = len( l.split() )
    outfile.write( "Words: " + str(wordcount) + ":" + l)
    # outfile.write('\n')

outfile.close()



infile = open('Three-years-in-europe.txt', 'r', encoding='utf-8')

for line in infile:
    print(line)

infile.close()