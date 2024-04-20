import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

new = pd.read_csv("new.csv")

cv = CountVectorizer(max_features=5000,stop_words='english')

vector = cv.fit_transform(new["tags"]).toarray()

similarity = cosine_similarity(vector)