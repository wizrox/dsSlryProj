'''
Author: Ken
git : https://github.com/PlayingNumbers/ds_salary_proj
Tutorial(youtube) : https://www.youtube.com/watch?v=QWgg4w1SpJ8&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t&index=6

Inspired by (Tutorial) : https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

Disclaimer: I don't own the copyrights of the code , It was written and coded as
            followed on the youtube channel as mentioned above, I have add extra comments for 
            my reference to make code understandable.please take a note that I have changed the names of the column and files according to my need
                   , if you are copy pasting this code you have to look for syntax errors in names of files and
                   data-columns that are used in tutorial.
'''
import flask
from flask import Flask, jsonify, request
import json
from data_input import data_in
import numpy as np
import pickle



def load_model():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled) 
        model = data['model']
    return model

app = Flask(__name__)
@app.route('/predict', methods=['GET'])    
def predict():
    # response = json.dumps({'response':'yahhh!'})
    # return response, 200
    # x = np.array(data_in).reshape(1,-1)
    
    request_json = request.get_json()
    x = request_json['input']
    print(x)
    x_in = np.array(x).reshape(1,-1)
    
    model = load_model()
    prediction = model.predict(x_in)[0]
    response = json.dumps({'response': prediction})
    return response, 200

if __name__ == '__main__':
    application.run(debug=True)