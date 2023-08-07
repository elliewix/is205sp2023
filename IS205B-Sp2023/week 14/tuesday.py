import json
import random
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)

print(info)
print(info[0]['name'])

for chunk in info:
    # print(chunk['name'])
    chunk['weight'] = random.randint(10,100)
    chunk['visits'] = {'num_visits': 0, 'notes': []}

chuck_visits = ['first visit', 'gave shots', 'ate a ball']
for note in chuck_visits:
    info[0]['visits']['num_visits'] += 1
    info[0]['visits']['notes'].append(note)

outfile = open('newinfo.json', 'w', encoding='utf-8')
json.dump(info, outfile, indent = 4)
outfile.close()

infile = open('newinfo.json', 'r', encoding='utf-8')
new_info = json.load(infile)
infile.close()

print(new_info)