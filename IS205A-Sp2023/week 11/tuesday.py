import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')

csvin = csv.reader(infile)
# print(csvin, type(csvin))
headers = next(csvin)

data = []
for row in csvin:
    data.append(row)

# print(next(csvin)) # error if you iterate on it

# print(headers)
# # print(data)
# for r in data:
#     print(r)

for r in data:
    print(r[1])  #get the 1th item, the name

names = [r[1] for r in data]

# print(names)

# writing out a csv


allrows = []

for r in data:
    # wikiid = r[0]
    # name = r[1]
    wikiid, name, *_ = r # more advanced
    newrow = [wikiid, name]
    allrows.append(newrow)

headers_out = ['wiki id', 'horse name']

# only when you have these things can you write otu the file

outfile = open('newhorses.csv', 'w', encoding='utf-8', newline='')

csvout = csv.writer(outfile)
csvout.writerow(headers_out) # needs 1D list
csvout.writerows(allrows) # needs a 2D list