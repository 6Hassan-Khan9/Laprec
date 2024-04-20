import pandas as pd

def recommend(tags, similarity):
  new_df = pd.read_csv("new.csv")
  for tag in tags:
    filt = new_df["tags"].str.contains(tag)
    new_df = new_df[filt]
  index = new_df[new_df["model"] == new_df["model"].values[0]].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
  for i in distances[1:6]:
    print(new.iloc[i[0]].model)