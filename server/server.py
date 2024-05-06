import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# Model imports --------------

import preprocessing as pp
from models import recommend as rcmd

# Server imports -------------

from flask import Flask, request, jsonify
from flask_cors import cross_origin

SERVER_LINK = "http://localhost:5000"
app = Flask(__name__)

# ---------------------------

# Starting the server

@app.route('/recommend', methods=['POST'])
@cross_origin()
def recommend_api():
  
  data = request.get_json()
  if not data:
    return jsonify({'error': 'NO DATA'}), 400
  
  search_tags = data.get('search_tags')
  if not search_tags:
    return jsonify({'error': 'MISSING TAGS'}), 400
  
  if not isinstance(search_tags, list):
    return jsonify({'error': 'INVALID FORMAT'}), 400
  
  # Run the algorithm
  result = rcmd.recommend(search_tags)
  return jsonify({'results': result})

app.run(debug=True)