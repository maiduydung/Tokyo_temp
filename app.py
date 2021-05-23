import pickle
import pandas as pd
import numpy as np
from flask import Flask, request
from datetime import date

def get_current_date():
    today = date.today()
    d = today.strftime("%Y-%m-%d")
    return d

app = Flask(__name__)
model = None


def load_model():
    global model
    with open('model_tokyo_temp.pkl','rb') as f:
        model = pickle.load(f)

@app.route("/")
def hello():
    return "hello world"

def print_text(text):
    return text

@app.route("/predict",methods=['POST','GET'])
def predict():
    if request.method == 'GET':
        results = model.fit()
        y_pred = results.predict(end=1300)
        index = pd.date_range(start='13/6/2018',periods=1301)
        y_pred.index = index
        curr_date = get_current_date()
    return "Current date " + str(curr_date)+ " Mean temperature " + str(round(y_pred[curr_date],2)) + " Celsius"
    

if __name__ == "__main__":
    load_model()
    app.run(debug=True)