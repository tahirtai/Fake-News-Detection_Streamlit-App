# train_model.py

import pandas as pd
import joblib
import string
import re
import nltk

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

# File paths
MODEL_FILE = "fake_news_model.pkl"
VECTORIZER_FILE = "tfidf_vectorizer.pkl"
LABEL_ENCODER_FILE = "label_encoder.pkl"
TRAIN_FILE = "train.csv"

# Preprocess text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = text.split()
    return " ".join([word for word in tokens if word not in stop_words])

# Load data
df = pd.read_csv(TRAIN_FILE)
df.dropna(subset=["title", "label"], inplace=True)
df["clean_title"] = df["title"].apply(clean_text)

# Encode labels
encoder = LabelEncoder()
df["label_encoded"] = encoder.fit_transform(df["label"])

# Features & labels
X = df["clean_title"]
y = df["label_encoded"]

# TF-IDF
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_vec = vectorizer.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(X_test))
print(f" Model trained with accuracy: {round(accuracy * 100, 2)}%")

# Save files
joblib.dump(model, MODEL_FILE)
joblib.dump(vectorizer, VECTORIZER_FILE)
joblib.dump(encoder, LABEL_ENCODER_FILE)

print(" Files saved: fake_news_model.pkl, tfidf_vectorizer.pkl, label_encoder.pkl")
