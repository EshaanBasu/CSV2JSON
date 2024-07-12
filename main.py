import csv
import json

def getValues(filename, label):
    dict = {}
    with open(filename, mode = 'r') as file:
        csvReader = csv.reader(file)
        for row in csvReader:
           if row[7] == label:
                dict.update({row[2]: [{'cui': row[3], 'score': row[4], 'label_semantic_types':row[5], 'label_ncts_counts': row[8]}]})
    return dict



c19Dict = {'covid-19': ['C5203670',{'have_had' : getValues('covid-19.csv', 'have_had')}, {'looking_for': getValues('covid-19.csv', 'looking_for')}]}
headachesDict = {'headaches': ['C0018681',{'have_had' : getValues('headaches.csv', 'have_had')}, {'looking_for': getValues('headaches.csv', 'looking_for')}]}
dyslexiaDict = {'dyslexia': ['C0476254',{'have_had' : getValues('dyslexia.csv', 'have_had')}, {'looking_for': getValues('dyslexia.csv', 'looking_for')}]}
anginaDict = {'angina': ['C0002962',{'have_had' : getValues('angina.csv', 'have_had')}, {'looking_for': getValues('angina.csv', 'looking_for')}]}
aneurysmDict = {'aneurysm': ['C002940',{'have_had' : getValues('aneurysm.csv', 'have_had')}, {'looking_for': getValues('aneurysm.csv', 'looking_for')}]}
cataractsDict = {'cataracts': ['0086543',{'have_had' : getValues('cataracts.csv', 'have_had')}, {'looking_for': getValues('cataracts.csv', 'looking_for')}]}
multiple_sclerosisDict= {'multiple scleorosis': ['C0026769',{'have_had' : getValues('multiple sclerosis.csv', 'have_had')}, {'looking_for': getValues('multiple sclerosis.csv', 'looking_for')}]}

print()
with open("covid-19.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("headaches.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("dyslexia.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("angina.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("cataracts.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("multiple_sclerosis.json", "w") as outfile:
    json.dump(c19Dict, outfile)

with open("aneurysm.json", "w") as outfile:
    json.dump(c19Dict, outfile)

print('output sent to json file')


