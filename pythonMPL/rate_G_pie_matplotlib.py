# rate G pie

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("titles.csv")

df.fillna(0,inplace = True)
gr_list = []
age_cer = {}
for l in range(5806):
  if df["age_certification"].loc[l] == "G":
    x = df["genres"].loc[l]
    x = x.split() 
    gr_list.append(x)
  
gr_list2 = []
for j in range(131):
  count = len(gr_list[j])
  while count != 0:
    gr_dt = gr_list[j][count-1]
    gr_dt = gr_dt.replace("[","")
    gr_dt = gr_dt.replace("]","")
    gr_dt = gr_dt.replace("'","")
    gr_dt = gr_dt.replace(",","")
    gr_list2.append(gr_dt)
    count -= 1

res = {}
for i in gr_list2:
    res[i] = gr_list2.count(i)

del res['']

sorted_dict = sorted(res.items(), key = lambda kv: kv[1], reverse = True)
sorted_dictionary = dict(sorted_dict)


list_res = list(sorted_dictionary.values())
print(list_res)

list_res_keys = list(sorted_dictionary.keys())
print("list res keys =",list_res_keys)

final_keys = []
final_values = []

for key,value in sorted_dictionary.items():
    if value > 25:
         print(key)
         final_keys.append(key)
         final_values.append(value)

print()
other_keys = []
other_values = []
for key,value in sorted_dictionary.items():
    if value < 43:
         print(key)
         other_keys.append(key)
         other_values.append(value)

final_other_values = sum(other_values)

final_keys.append("other")
final_values.append(final_other_values)

print(sorted_dictionary)
print(final_keys)
print(final_values)

colors = ["#82E0AA","#52BE80","#229954","#117A65","#0E6655"]
plt.figure(figsize = (3,2))
wedgeprops = {"linewidth": 1, 'width':1, "edgecolor":"k"}
plt.pie(final_values,autopct='%0.2f%%', explode=[0.2,0.1,0.1,0.075,0.075],labels = final_keys, shadow = True
        , wedgeprops = wedgeprops, frame=True,center=(2, 3), labeldistance = 1.3, radius = 1, colors = colors)
plt.legend()
plt.title("rate G")
plt.show()
