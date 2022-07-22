#Genres Categories
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("titles.csv")

gr_list = []
for i in range(5806):
  x = df['genres'].loc[i]
  x = x.split()
  gr_list.append(x)

gr_list2 = []
for j in range(5806):
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

color = ['forestgreen','limegreen','darkgreen','green','lime','seagreen','springgreen','aquamarine','turquoise','lightseagreen','mediumturquoise','lightcyan','paleturquoise','teal','aqua','cyan','cadetblue','powderblue','lightblue']
plt.rcParams.update({'font.size': 45})
fig = plt.figure(figsize=(16,10))
ax = fig.add_axes([0,0,5,3])

list_res = list(res.values())
for index, value in enumerate(list_res):
  plt.text(index, value,str(value),ha='center',va='bottom')

ax.bar(range(len(res)), list(res.values()), align='center' ,color = color)
plt.xticks(range(len(res)), list(res.keys()))
plt.xlabel("Genres",fontsize=50,fontweight="heavy",va='top')
plt.title("Genres Categories",fontsize=80,fontweight="bold")

plt.show()
