import joblib

model = joblib.load("models/chatbot_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def get_response(user_input):
    X_test = vectorizer.transform([user_input])
    response = model.predict(X_test)[0]
    return response
