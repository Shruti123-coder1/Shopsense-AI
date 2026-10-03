from flask import Flask, render_template, request
from model import get_response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat")
def chat():
    msg = request.args.get("msg")
    if not msg:
        return "Please ask a question."
    reply = get_response(msg)
    return reply

# 👇 IMPORTANT FOR RENDER / DEPLOYMENT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port)