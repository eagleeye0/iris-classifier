from flask import Flask, request, render_template
import pickle
import time
import numpy as np

app = Flask(__name__)
with open('iris_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def front_page():
    return render_template('index.html',values = 'python')

@app.route('/', methods=['POST'])
def prediction():
    val = np.array([x for x in request.form.values()])
    val = val[:-1]
    for i in range(len(val)):
        val[i] = int(val[i])
    val = val.reshape(1,-1)
    pred = np.array(model.predict(val))
    if pred[0][0] == 1 and pred[0][1] == 0:
        pred = 'Iris-virginica'
    if pred[0][0] == 0 and pred[0][1] == 1:
        pred = 'Iris-versicolor'
    if pred[0][0] == 0 and pred[0][1] == 0:
        pred = 'Iris-setosa'
    return render_template('index.html', values=pred)
