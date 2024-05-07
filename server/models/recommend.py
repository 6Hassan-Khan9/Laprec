import pandas as pd
import os
from models import bagOfWords as bw

def recommend(tags):
  laptops = pd.read_csv(os.path.join("server", "db", "laptops.csv"))
  filteredByTags = laptops
  
  for tag in tags:
    filt = filteredByTags["tags"].str.contains(tag)
    filteredByTags = filteredByTags[filt]

  # choose the index of the best laptop which matches the tags and find the similarity of other 
  # laptops relative to it
  index = filteredByTags[filteredByTags["model"] == filteredByTags["model"].values[0]].index[0]
  distances = sorted(list(enumerate(bw.similarity[index])),reverse=True,key = lambda x: x[1])

  # print the best laptops which strictly match the tags
  showHowMany = 5
  alreadyListed = []
  result = []

  for i in distances:
    if i[0] in filteredByTags.index:
      # print(filteredByTags.loc[i[0]]['model'])
      alreadyListed.append(i[0])
      result.append(filteredByTags.loc[i[0]]['model'])

    if len(alreadyListed) >= showHowMany:
        break
  
  # print the next best laptops which don't strictly match the tags 
  if len(alreadyListed) < showHowMany:
    count = len(alreadyListed)
    for i in distances:
      if i[0] not in alreadyListed:
        # print(laptops.loc[i[0]]["model"])
        result.append(laptops.loc[i[0]]["model"])
        count += 1
      if count >= showHowMany:
        break
  
  return result