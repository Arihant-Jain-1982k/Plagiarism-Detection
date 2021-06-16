import pandas as pd
import re
import numpy as np

lookup = {}
for i in range(26):
    temp_frame = pd.read_csv('Embeddings/' + chr(ord('a') + i) + '.csv')
    lookup[chr(ord('a') + i)] = temp_frame
numeric = pd.read_csv("Embeddings/numeric.csv")
lookup["num"] = numeric
data = pd.read_csv("Embeddings/Embeddings.txt", delimiter = " ")

def find(word):
    init = word[0]
    apos = 13
    if init.isnumeric():
        look = lookup['num']
        if word in look['STRING'].values:
            index = int(look[look['STRING'] == word].INDEX.values)
            return index
        else:
            return -1;
    if init == "'":
        return apos
    else:
        look = lookup[init]
        if word in look['STRING'].values:
            index = int(look[look['STRING'] == word].INDEX.values)
            return index
        else:
            return -1
    return -1

def vectorize(sentence):
    sentence = re.split('[,. ?!()"@#;:%$&*-/]', sentence)
    for i in range(len(sentence)):
        sentence[i] = sentence[i].lower()
        if sentence[i][-2:] == "'s":
            sentence.insert(i+1, "'s")
            sentence.insert(i+1, sentence[i][:len(sentence[i])-2])
            sentence.remove(sentence[i])
    while '' in sentence:
        sentence.remove('')
    for i in range(len(sentence)):
        word = sentence[i]
        if word != "'s":
            if "'" in word:
                troph = word.replace("'", '')
                sentence.insert(i+1, troph)
                sentence.remove(sentence[i])
    vector = np.array([], ndmin = 2)
    for word in sentence:
        index = find(word)
        vector.append(index)
        if index == -1:
            vector = np.append(vector, np.zeros(1, 300))
        else:
            vector = np.append(vector, data.iloc[index, 1:].values.tolist())
    return sentence, vector
    
s, v = vectorize('There is no person playing a piano Tatvarishi')
print(s)
print(v)