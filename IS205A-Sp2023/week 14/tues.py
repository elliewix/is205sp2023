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

# jdata = json.loads(data)

infile = open('data.json', 'r', encoding='utf-8')
jdata = json.load(infile)
infile.close()

# print(jdata[0])
for d in jdata:
    # print(d)
    d['weight'] = random.randint(5,100)
    d['visits'] = {'num_visits': 0, 'notes': []}
    # print(d)

# jdata[0]['visits']['num_visits'] += 1

chuck_notes = ['first visit, fine', 'followup, did bloodwork', 'gave shots']
chuck_i = 0 # he's the 0th dict in jdata

for note in chuck_notes:
    jdata[chuck_i]['visits']['num_visits'] += 1
    jdata[chuck_i]['visits']['notes'].append(note)

brent_notes = ['first visit, normal', 'ate a sock, threw it up', 'ate a ball']

for note in brent_notes:
    # brent is in pos 1
    jdata[1]['visits']['num_visits'] += 1 # numvisits is int, so add 1
    jdata[1]['visits']['notes'].append(note) # notes is a list, so append


outfile = open('newdata.json', 'w', encoding='utf-8')
json.dump(jdata, outfile, indent = 4)
outfile.close()

