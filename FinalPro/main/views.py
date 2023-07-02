from django.shortcuts import render
from django.http import HttpResponse
from main.alco_re import *
import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance_matrix
from scipy.spatial.distance import squareform
from sklearn.preprocessing import MinMaxScaler
from string import punctuation
import re
import json
# Create your views here.

def index(request) :
    result = recom('서울의 밤')
    # print(result)
    context = {"result" : result }
    return render(request, 'main/index.html', context)

def alc_recomm() :
    result = recom('서울의 밤')
    context = {"result" : result }
    # print(result)
    # return HttpResponse("main 페이지 입니다")
    # return render(request, 'main/alc.html', context)

alc_recomm()
