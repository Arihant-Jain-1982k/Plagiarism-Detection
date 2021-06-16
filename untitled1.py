import XMLDocument as xml
import pandas as pd
import numpy as np

source = []

for i in range(11093):
    doc = xml.Document(i)
    print(i)
    doc.parse()
    source.append(doc)
    
sus = []

for i in range(750):
    doc = xml.Document(i, Type = "suspicious")
    print(i)
    doc.parse()
    sus.append(doc)
    
x_train = pd.read_csv("Dataset/Plag/X_train.csv", index_col=0)
x_test = pd.read_csv("Dataset/Plag/X_test.csv", index_col=0)
base = np.zeros((1, 47158))
for i in range(len(x_train)):
    a = np.load(sus[x_train.iloc[i]['SUS'].astype("int")-1].name + "_score.npy")
    b = np.load(source[x_train.iloc[i]['SOURCE'].astype("int")-1].name + "_score.npy")
    a = np.concatenate((a,b)).reshape((1, 47158))
    base = np.concatenate((base,a))
    print(i)
base = np.delete(base, 0, 0)

base1 = np.zeros((1, 47158))
for i in range(len(x_test)):
    a = np.load(sus[x_test.iloc[i]['SUS'].astype("int")-1].name + "_score.npy")
    b = np.load(source[x_test.iloc[i]['SOURCE'].astype("int")-1].name + "_score.npy")
    a = np.concatenate((a,b)).reshape((1, 47158))
    base1 = np.concatenate((base1,a))
    print(i)
base1 = np.delete(base1, 0, 0)

np.save("Dataset/Plag/X_train.npy", base)
np.save("Dataset/Plag/X_test.npy", base1)