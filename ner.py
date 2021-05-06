import numpy as np
import json
import spacy
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

nlp = spacy.load('model')
with open(input_file,'r') as f:
    paragraph = f.read()

doc = nlp(paragraph)

name_entity = []   #to store entity and its label
labels = ['living_entity', 'place', 'object']
for ent in doc.ents:
    name_entity.append([str(ent),ent.label_])
    
name_entity = np.array(name_entity)
name_entity = np.unique(name_entity, axis=0)

entities = {}
for i in labels:
    rows,cols = np.where(name_entity == i)
    entities[i] = list(name_entity[rows,0])

res = {'entities':entities}
with open(output_file,'w') as f:
    json.dump(res,f)