import pandas as pd
import time

t1 = time.perf_counter_ns()
data = pd.read_csv("List.csv", names = ['INDEX', 'STRING'])
t2 = time.perf_counter_ns()
sort = data.sort_values(by=['STRING'], kind="mergesort", ignore_index=True)
t3 = time.perf_counter_ns()
num = pd.DataFrame(columns=['INDEX', 'STRING'])
Alpha = pd.DataFrame(columns=['FRAME'])
blank = pd.DataFrame(columns=['INDEX', 'STRING'])
chars = 'abcdefghijklmnopqrstuvwxyz'

for i in range(26):
    Alpha = Alpha.append({'FRAME':blank}, ignore_index=True)

for i in sort.iterrows():
    print(i[0]) 
    print(str(i[1].STRING).lower()[0])    
    if(str(i[1].STRING)[0].isnumeric()):
        num = num.append(i[1])
    if(str(i[1].STRING)[0] in chars):
        Alpha.iloc[ord(str(i[1].STRING).lower()[0]) - ord('a')]['FRAME'] = Alpha.iloc[ord(str(i[1].STRING)[0]) - ord('a')]['FRAME'].append(i[1])
        
t4 = time.perf_counter_ns()

for i in range(26):
    blank = Alpha.iloc[i]['FRAME']
    blank.to_csv(chr(ord('a') + i) + '.csv', index = False)
    
num.to_csv("Numeric.csv", index = False)

t5 = time.perf_counter_ns()

print("Read Time: ", str((t2-t1)/pow(10, 9)))
print("Sort Time: ", str((t3-t2)/pow(10, 9)))
print("Run Time: ", str((t4-t3)/pow(10, 9)))
print("Write Time: ", str((t5-t4)/pow(10, 9)))