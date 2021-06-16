import XMLDocument as xml
import pandas as pd
import numpy as np
from numba import jit
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

sus = []
sources = []
source = []

for i in range(750):
    doc = xml.Document(i, Type = "suspicious")
    print(i)
    doc.parse()
    sus.append(doc)
    sources = sources + doc.source_doc
    
sources = sorted(list(set(sources)))

for i in sources:
    doc = xml.Document(i-1)
    print(i)
    doc.parse()
    source.append(doc)
   
      
check = []
    
for i in range(750):
    file = open(sus[i].name + ".txt", encoding = "utf8").read()
    file = len(tokenizer.tokenize(file))
    print(i)
    if file<=500:
        check.append(i)

source_check = []
for i in range(1030):
    file = open(source[i].name + ".txt", encoding = "utf8").read()
    file = len(tokenizer.tokenize(file))
    print(i)
    if file<=500:
        source_check.append(i)

source_list  =[]

for i in range(11093):
    doc = xml.Document(i)
    print(i)
    doc.parse()
    source_list.append(doc)
    
for i in check:
    file = np.load(sus[i].name + "_score.npy")
    s = slice(500, 23579)
    file = np.delete(file, s, 0)
    np.save(sus[i].name + "_score1.npy", file)
    print(i)

for i in source_check:
    file = np.load(source_list[sources[i]-1].name + "_score.npy")
    s = slice(500, 23579)
    file = np.delete(file, s, 0)
    np.save(source_list[sources[i]-1].name + "_score1.npy", file)
    print(i)
        
