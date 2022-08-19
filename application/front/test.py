import pandas as pd
import requests
import json


data_dict = {
    'time_in_hospital': 3,
    'num_lab_procedures': 2,
    'num_procedures': 2,
    'num_medications' : 2,
    'number_outpatient': 2,
    'number_emergency' : 2,
    'number_inpatient': 2,
    'number_diagnoses' : 2,
    'age' : 34
    }

response = requests.post("http://127.0.0.1:8000/prediction", json=data_dict)
print(response)
# response = requests.post("http://127.0.0.1:8000/docs#/default/predict_prediction_post", json=data_dict)
#response = requests.post("http://172.18.0.3:30000/predict", json=data)
prediction = response.text
print(type(prediction))
