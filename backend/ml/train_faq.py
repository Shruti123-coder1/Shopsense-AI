import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("ecommerce_faq.csv")

questions = df["question"]
answers = df["answer"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = LogisticRegression(max_iter=200)
model.fit(X, answers)

joblib.dump(model, "models/chatbot_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model trained and saved!")
