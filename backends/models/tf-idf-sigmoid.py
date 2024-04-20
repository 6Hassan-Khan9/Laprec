import pandas as pd
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

new = pd.read_csv("new.csv")

tfidf = TfidfVectorizer(max_features=5000,stop_words='english')

matrix = tfidf.fit_transform(new["tags"])

similarity = sigmoid_kernel(matrix, matrix)