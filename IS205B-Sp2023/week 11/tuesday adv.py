import csv

with open('horse csv example.csv','r', encoding='utf-8') as infile:
    # headers, *data = csv.reader(infile)
    csvin = csv.reader(infile)
    headers = next(csvin)
    data = [r for r in csvin]

print(headers)
print(data[:4])