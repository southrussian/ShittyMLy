import pandas as pd
import textblob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import spacy
import plotly.express as px
from collections import defaultdict
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# nlp = spacy.load('en_core_web_sm')

data = pd.read_csv("articles.csv", encoding='latin-1')
print(data.head())
