import csv

infile = open('horse csv example.csv', 'r', encoding='utf-8')

csvin = csv.reader(infile)
# print(csvin, type(csvin))
headers = next(csvin)
# print(headers)
data = []
for r in csvin:
    data.append(r)
print(data[:4])

####

newrows = [] # my 2d list of data

for row in data:
    horseid = row[0] #0th item
    name = row[1] # 1th item
    # horseid, name, *_ = row
    newrow = [name, horseid] #collect this!
    newrows.append(newrow)

# print(newrows)
headers = ['horse name', 'horse wiki id']

# now we can write

outfile = open('new horses.csv', 'w', encoding='utf-8', newline='')

csvout = csv.writer(outfile)
csvout.writerow(headers) # 1d list
csvout.writerows(newrows) # 2d list