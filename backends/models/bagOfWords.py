import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

laptops = pd.read_csv("laptops.csv")

cv = CountVectorizer(max_features=5000,stop_words='english')

vector = cv.fit_transform(laptops["tags"]).toarray()

similarity = cosine_similarity(vector)