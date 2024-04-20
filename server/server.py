import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Server imports -------------

from flask import Flask, request, jsonify

SERVER_LINK = "http://localhost:5000"
app = Flask(__name__)

# ---------------------------

pd.set_option('display.max_colwidth', None)      

laptops = pd.read_csv("model/data.csv")

laptops.rename(columns={"Model": "model", "Price": "price", "Rating": "rating"}, inplace=True)

laptops.drop(columns=["secondary_storage_type"], inplace=True)

laptops.sort_values(by=["rating", "price"], ascending=[False, True], inplace=True)

laptops = laptops.astype(str)

laptops["tags"] = laptops[["brand", "processor_brand", "processor_tier", "num_cores", "ram_memory", "primary_storage_type",
                           "primary_storage_capacity", "gpu_brand", "gpu_type", "display_size"]].apply(lambda x: ' '.join(x), axis = 1)

laptops["id"] = laptops.index

new = laptops[["id", "model", "tags"]]
new.index = range(len(new))

# Model

cv = CountVectorizer(max_features=5000,stop_words='english')

vector = cv.fit_transform(new["tags"]).toarray()

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)

# RECOMMENDER

def recommend(tags):

  recommended_models = []

  new_df = new.copy()
  for tag in tags:
    filt = new_df["tags"].str.contains(tag)
    new_df = new_df[filt]
  index = new_df[new_df["model"] == new_df["model"].values[0]].index[0]
  distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
  for i in distances[1:6]:
    recommended_models.append(new.iloc[i[0]].model)

  return recommended_models

# Starting the server

@app.route('/recommend', methods=['POST'])
def recommend_api():
  
  data = request.get_json()
  if not data:
    return jsonify({'error': 'NO DATA'}), 400
  
  search_tags = data.get('search_tags')
  if not search_tags:
    return jsonify({'error': 'MISSING TAGS'}), 400
  
  if not isinstance(search_tags, list):
    return jsonify({'error': 'INVALID FORMAT'}), 400
  
  result = recommend(search_tags)
  return jsonify({'results': result})

app.run(debug=True)