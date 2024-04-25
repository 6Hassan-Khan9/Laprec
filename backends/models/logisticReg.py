import pandas as pd
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

laptops = pd.read_csv("../db/laptops.csv")

tfidf = TfidfVectorizer(max_features=5000,stop_words='english')

matrix = tfidf.fit_transform(laptops["tags"])

similarity = sigmoid_kernel(matrix, matrix)