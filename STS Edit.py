import pandas as pd

def split(data, test = 0.1, dev= 0.1):
    num = int(data.shape[0]*dev)
    t = data.sample(frac = test)
    data = data.drop(t.index)
    d = data.sample(frac = num/data.shape[0])
    data = data.drop(d.index)
    return data, t, d

data = pd.read_csv("Dataset/STS/STS Pairs.txt")
data = data.drop(columns = ["pair_ID", "entailment_judgment"])
data.rename(columns = {"sentence_A" : "A", "sentence_B" : "B", "relatedness_score": "SCORE"}, inplace=True)
data.SCORE = (data.SCORE-1)/4
data.to_csv("Dataset/STS/STS.csv", index=False)
data, t, d = split(data, test = .05, dev = .05)

data.to_csv("Dataset/STS/STS_Train.csv", index = False)
t.to_csv("Dataset/STS/STS_Test.csv", index = False)
d.to_csv("Dataset/STS/STS_Dev.csv", index = False)
