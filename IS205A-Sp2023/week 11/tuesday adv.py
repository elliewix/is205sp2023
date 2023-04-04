import csv

with open('horse csv example.csv', 'r', encoding='utf-8') as infile:
    # headers, *data = csv.reader(infile) # very short but does it
    csvin = csv.reader(infile)
    headers = next(csvin)
    data = [r for r in csvin]



print(headers)
print(data[:4])