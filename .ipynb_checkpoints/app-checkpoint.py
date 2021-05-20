import pickle
from flask.json import load
import numpy as np
from flask import Flask, request


model = None
app = Flask(__name__)

def load_model():
    global model
    # model variable refers to the global variable
    with open('model_tokyo_temp.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return "hi"

@app.route('/hello')
def hello():
    return 'Hello, World'
    

@app.route('/predict', methods=['POST','GET'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data = request.get_json()  # Get data posted as a json
        print(data)
    #     data = np.array(data)[np.newaxis, :]  # converts shape from (4,) to (1, 4)
    #     prediction = model.predict(data)  # runs globally loaded model on the data
    return "AAAAA"

if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=80)
