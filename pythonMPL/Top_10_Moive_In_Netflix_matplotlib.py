#Top 10 Moive In Netflix
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import csv

score = {}

with open('titles4.csv', mode='r') as inp:
    reader = csv.reader(inp)
    score = {rows[1]:rows[11] for rows in reader}

score.pop('title')
print(score)

movie = []


for i in range(10):
  val = max(score, key= lambda x: score[x])
  print("movie :",val)
  movie.append(val)
  
  new_val = score.values()
  maximum_val = float(max(new_val))
  print("imdb:",maximum_val)
  print("---------------")
  movie.append(maximum_val)
  del score[val]

def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
         

movie2 = Convert(movie)


color = ['forestgreen','limegreen','darkgreen','green','lime','seagreen','springgreen','aquamarine','turquoise','lightseagreen']
plt.rcParams.update({'font.size': 30})
fig = plt.figure(figsize=(16,10))
ax = fig.add_axes([0,0,5,3])

list_res = list(movie2.values())
for index, value in enumerate(list_res):
  plt.text(index, value,str(value),fontsize=40,ha='center',va='bottom')

ax.bar(range(len(movie2)), list(movie2.values()), align='center' ,color = color)
plt.ylim(8, 9.5)
plt.xticks(range(len(movie2)), list(movie2.keys()))
plt.xlabel("Movie Titles",fontsize=30,fontweight="heavy",va='top')
plt.ylabel("IMDB Score",fontsize=30,fontweight="heavy",va='bottom')
plt.title("Top 10 Moive In Netflix",fontsize=80,fontweight="bold")

plt.show()
