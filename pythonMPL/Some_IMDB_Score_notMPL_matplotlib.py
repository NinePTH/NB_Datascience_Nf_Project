#Some IMDB score
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import Counter

new_data_dict = {}
with open("titles4.csv", 'r') as data_file:
    data = csv.DictReader(data_file, delimiter=",")
    for row in data:
        item = new_data_dict.get(row["genres"], dict())
        item[row["title"]] = (row["imdb_score"])

        new_data_dict[row["genres"]] = item

print(new_data_dict)



print("----------------")
for i in range(10):
  
  new_out = {}
  for new_k, new_v in new_data_dict.items():
    count_new = 0
    for element in new_v.values():
      element2 = float(element)
      if element2 > count_new:
        count_new = element2
    new_out[new_k] = count_new
  
  val = max(new_out, key= lambda x: new_out[x])
  print("genres :",val)

  dict2 = new_data_dict[val]

  val2 = max(dict2, key= lambda x: dict2[x])
  print("title :",val2)

  new_val = new_out.values()
  maximum_val = max(new_val)
  print("imdb score:",maximum_val)
  print("----------------")
  del new_data_dict[val][val2]

