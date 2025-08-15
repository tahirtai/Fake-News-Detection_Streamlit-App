# fake_news_detector.py

import streamlit as st
import pandas as pd
import numpy as np
import string
import joblib
import os
import re
import nltk
import plotly.express as px

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

# ------------------ Global Constants ------------------
MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"
LABEL_ENCODER_FILE = "label_encoder.pkl"
TRAIN_FILE = "train.csv"

# ------------------ Download NLTK Stopwords ------------------
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

# ------------------ Text Preprocessing ------------------
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return " ".join([word for word in tokens if word not in stop_words])

# ------------------ Model Training or Loading ------------------
@st.cache_resource
def load_model():
    model = joblib.load(MODEL_FILE)
    vectorizer = joblib.load(VECTORIZER_FILE)
    encoder = joblib.load(LABEL_ENCODER_FILE)
    return model, vectorizer, encoder

# ------------------ Prediction Function ------------------
def predict_news(text, model, vectorizer, encoder):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    confidence = model.predict_proba(vec)[0][prediction] * 100
    # Use label map for clear string output
    label_map = {0: "REAL", 1: "FAKE"}
    predicted_label = label_map[prediction]
    return predicted_label, confidence

# ------------------ Streamlit App ------------------
def main():
    st.set_page_config(page_title="Fake News Detector", layout="centered")
    st.title(" Fake News Detector")
    st.markdown("Use Machine Learning to detect **Fake News** from headlines.")

    model, vectorizer, encoder = load_model()

    st.header("🔍 Test a News Headline")
    user_input = st.text_input("Enter a news headline here:")

    if user_input:
        label, confidence = predict_news(user_input, model, vectorizer, encoder)
        st.markdown(f"**Prediction:** `{label}`")
        st.markdown(f"**Confidence:** `{round(confidence, 2)}%`")

        if label == "FAKE":
            st.error(" Warning: This may be FAKE news.")
        else:
            st.success(" This appears to be REAL news.")

    st.header("📂 Upload CSV File")
    uploaded_file = st.file_uploader("Upload CSV file with a `title` column", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)

            if 'title' not in df.columns:
                st.error("The CSV must have a column named `title`.")
                return

            df['clean_title'] = df['title'].apply(clean_text)
            vecs = vectorizer.transform(df['clean_title'])
            predictions = model.predict(vecs)
            confidences = model.predict_proba(vecs).max(axis=1) * 100

            label_map = {0: "REAL", 1: "FAKE"}
            df['prediction'] = [label_map[p] for p in predictions]
            df['confidence'] = confidences

            st.subheader(" Prediction Results")
            st.dataframe(df[['title', 'prediction', 'confidence']].head(20))

            st.subheader(" Prediction Summary")
            chart_df = df['prediction'].value_counts().reset_index()
            chart_df.columns = ['Label', 'Count']

            col1, col2 = st.columns(2)
            with col1:
                st.plotly_chart(px.pie(chart_df, names='Label', values='Count', title="Fake vs Real Distribution"), use_container_width=True)
            with col2:
                st.plotly_chart(px.bar(chart_df, x='Label', y='Count', color='Label', title="Prediction Count"), use_container_width=True)

            csv_out = df[['title', 'prediction', 'confidence']].to_csv(index=False).encode()
            st.download_button(" Download CSV Results", csv_out, "predictions.csv", "text/csv")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
