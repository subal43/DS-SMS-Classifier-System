import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import string 
import nltk
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
tfv = TfidfVectorizer(max_features=2500)
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    l = []
    for i in text:
        if i.isalnum():
            l.append(i)
    text = l.copy()
    l.clear()
    for i in text :
        if i not in stopwords.words('english') and i not in string.punctuation:
            l.append(ps.stem(i))
    return " ".join(l)
            
    
st.markdown(
    "<h1 style='text-align: center;'>SMS Classifier</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; font-size: 20px; margin-top: -10px;'>A simple web app to classify SMS messages as spam or ham.</div><br>",
    unsafe_allow_html=True
)
st.divider()
txt = st.text_area("Enter your SMS message here:", height=150)
transformed_txt = transform_text(txt)
vector_input = tfv.fit_transform([transformed_txt])
prediction = model.predict(vector_input)[0]


if st.button("Classify Message"):
    st.write("Prediction:", "Spam" if prediction == 1 else "Ham")

st.markdown(
    "<br><br><br><div style='text-align: center; margin-top: 20px; color: gray;'>Developed by Your Subal Kundu</div>",
    unsafe_allow_html=True
)