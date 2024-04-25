import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

laptops = pd.read_csv("../db/laptops.csv")

tfidf = TfidfVectorizer(max_features=5000,stop_words='english')

matrix = tfidf.fit_transform(laptops["tags"])

similarity = linear_kernel(matrix, matrix)