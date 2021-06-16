import pandas as pd
import re
import numpy as np
import gc

#Code to generate lookup dictionary and import word vectors

lookup = {}
for i in range(26):
    temp_frame = pd.read_csv('Embeddings/' + chr(ord('a') + i) + '.csv')
    lookup[chr(ord('a') + i)] = temp_frame
numeric = pd.read_csv("Embeddings/numeric.csv")
lookup["num"] = numeric
frame = pd.read_csv("Embeddings/Embeddings.txt", delimiter = " ")

#Function to find word to index mapping from lookup dictionary

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
    if ord(init)>=97 and ord(init)<=122 :
        look = lookup[init]
        if word in look['STRING'].values:
            index = int(look[look['STRING'] == word].INDEX.values)
            return index
        else:
            return -1
    return -1

#Function to convert sentence into corresponding array of word vectors

def vectorize(sentence, returns = "both"):
    sentence = re.split('[,. ?!()"@#;:%$&*-/<>]', sentence)
    for i in range(len(sentence)):
        if sentence[i][-2:] == "'s":
            sentence.insert(i+1, "'s")
            sentence.insert(i+1, sentence[i][:len(sentence[i])-2])
            sentence.remove(sentence[i])
                    
    for i in range(len(sentence)):
        word = sentence[i]
        if word != "'s":
            if "'" in word:
                troph = word.replace("'", '')
                sentence.insert(i+1, troph)
                sentence.remove(sentence[i])
                
    while '' in sentence:
        sentence.remove('')
                
    if returns == "words":
        return sentence
                
    if returns == "vector" or returns =="both":
        vector = np.array([])
        for word in sentence:
            index = find(word)
            if index == -1:
                vector = np.append(vector, np.zeros((1, 300)))
            else:
                vector = np.append(vector, frame.iloc[index, 1:].values.tolist())
        vector = np.reshape(vector, (1, len(sentence), 300))
        if returns == "vector":
            return vector
        else:
            return sentence, vector
        
    else:
        return "Incorrect Return Query!"

#Function to pad the smaller input to size of larger input with 0s

def padding(output_1, output_2):

    pad = output_1.shape[0] - output_2.shape[0]

    if pad>0:
        Pad = np.zeros((pad, 1))
        output_2 = np.append(output_2, Pad)
        return output_2
    
    if pad<0:
        Pad = np.zeros((abs(pad), 1))
        output_1 = np.append(output_1, Pad)
        return output_1
    return output_1

#Function to convert input DataFrame[A, B, SCORE] into vector dataset

def translate_x(data):
    length = list()
    for i in range(len(data.A)):
        length.append(len(vectorize(data.iloc[i][0], returns = "words")))
        length.append(len(vectorize(data.iloc[i][1], returns = "words")))
    LEN = max(length)
    pad_array = np.zeros((1, LEN, 1))
    
    translation = np.array([])
    
    for i in range(len(data.A)):
        
        vector = vectorize(data.iloc[i][0], returns = 'vector')
        vector = padding(vector, pad_array)
        translation = np.append(translation, vector)
        
        vector = vectorize(data.iloc[i][1], returns = 'vector')
        vector = padding(vector, pad_array)
        translation = np.append(translation, vector)
        
    translation = translation.reshape((len(data.A)*2, LEN, 300))
        
    return translation

#Function to convert input DataFrame[A, B, SCORE] into output labels

def translate_y(data):
    y = np.array([])
    for i in range (len(data.A)):
        y = np.append(y, float(data.iloc[i][2]))
        y = np.append(y, 0)
    y = y.reshape((2*len(data.A), 1)).astype('float')
    return y

#Function to deallocate the memory being used by word vector file

def deallocate():
    global frame
    del frame
    gc.collect()