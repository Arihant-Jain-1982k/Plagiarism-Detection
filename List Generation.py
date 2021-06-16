import pandas as pd
import time

t1 = time.perf_counter_ns()
data = pd.read_csv("Embeddings/Embeddings.txt", delimiter=" ", header = None)
t2 = time.perf_counter_ns()
print("Read Time: " + str((t2-t1)/pow(10, 9)))
entries = []

for i in data.iloc[:, 0]:
    entries.append(i)

entries = pd.DataFrame(entries, columns=['Strings'])
t3 = time.perf_counter_ns()
print("Indexing Time: " + str((t3-t2)/pow(10, 9)))
entries.to_csv("Embeddings/List.csv")
t4 = time.perf_counter_ns()
print("Write Time: " + str((t4-t3)/pow(10, 9)))
