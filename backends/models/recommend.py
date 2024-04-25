import pandas as pd
from bagOfWords import similarity

def recommend(tags):
  laptops = pd.read_csv("laptops.csv")
  filteredByTags = laptops
  
  for tag in tags:
    filt = filteredByTags["tags"].str.contains(tag)
    filteredByTags = filteredByTags[filt]

  # choose the index of the best laptop which matches the tags and find the similarity of other 
  # laptops relative to it
  index = filteredByTags[filteredByTags["model"] == filteredByTags["model"].values[0]].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

  # print the best laptops which strictly match the tags
  showHowMany = 5
  alreadyListed = []

  for i in distances:
    if i[0] in filteredByTags.index:
      print(filteredByTags.loc[i[0]])
      alreadyListed.append(i[0])

    if len(alreadyListed) >= showHowMany:
        break
  
  # print the next best laptops which don't strictly match the tags 
  if len(alreadyListed) < showHowMany:
    count = len(alreadyListed)
    for i in distances:
      if i[0] not in alreadyListed:
        print(laptops.loc[i[0]])
        count =+ 1
      if count >= showHowMany:
        break