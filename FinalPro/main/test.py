import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance_matrix
from scipy.spatial.distance import squareform
from sklearn.preprocessing import MinMaxScaler
from string import punctuation
import re

alco = pd.read_csv('alcohol_df_1.csv')

flavour = alco['맛'].fillna('')

print(flavour[0])
print(type(flavour))
# flavour 코사인 유사도 구하기
# instantiating and generating the count matrix
count = CountVectorizer()
count_matrix = count.fit_transform(flavour)

# generating the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)

# 확인
print(cosine_sim)