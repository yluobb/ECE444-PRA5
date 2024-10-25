from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import json

application = Flask(__name__)

with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)  

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/predict", methods=["POST"])
def prediction():
    data = request.get_json()
    texts = data["input"]
    results = [loaded_model.predict(vectorizer.transform([text]))[0] for text in texts]


    # Perform prediction
    # prediction = loaded_model.predict(vectorizer.transform(texts))

    # Return the prediction result as JSON
    return jsonify({"prediction": results}), 200
    
# 
if __name__ == "__main__":
    application.run(port=5000, debug=True)
