import numpy as np
import pandas as pd
import os
import re
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder ,LabelEncoder
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# from textblob import TextBlob
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# nltk.download('stopwords')
# from nltk.stem import PorterStemmer
# from nltk.stem import WordNetLemmatizer


class TextPreprocessing:
    def __init__(self,data:pd.DataFrame):
        self.data = data
        self.X_train = None
        self.y_test = None
        self.y_train = None
        self.y_test = None
    
    def encoding(self,data):
        encode = LabelEncoder()
        return encode.fit_transform(data)
    
    def train_test_split(self):
        X = self.data['text']
        y = self.data['sentimate']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)
        self.X_train,self.X_test,self.y_train,self.y_test = X_train,X_test,y_train,y_test
        return X_train,X_test,y_train,y_test
    
    def preproccess(text):
        # Lowercassing
        text = text.lower()
        # Remove links
        patt = r"http[s]?://\S+"
        text = re.sub(patt,"",text)
        # Remove Numbers
        text = re.sub(r"\d+", "", text)
        # Remove HTML tags
        text = re.sub(r"<.*?>", "", text)
        # Remove Symbols
        text = re.sub(r'[^\w\s]|\n\n|\n|\\', ' ', text)
    
    # def text_vectorization(text):
    def model_train():
        
        
        
        
        
        
        
        
        
        
        
        
# # Tokenization
# blob = TextBlob(text)
# # remove white space
# clean = [w.strip() for w in clean]
# # Remove Duplicates
# text = {w for w in clean}
# # Remove stop word
# stop_words = set(stopwords.words('english'))
# text_str = " ".join(text)
# tokens = word_tokenize(text_str)
# # Stemming
# ps = PorterStemmer()
# stemmed = [ps.stem(w) for w in tokens]
# # Lemmatization
# nltk.download('wordnet')
# lemmatizer = WordNetLemmatizer()
# lemmas = [lemmatizer.lemmatize(w, pos="v") for w in stemmed]
# # Unique words
# text = {w for w in lemmas}
# text = list(text)
# # Spelling Correction
# text_str2 = " ".join(text)
# blob = TextBlob(text_str2)
# corrected = str(blob.correct())

# text = corrected.split()


