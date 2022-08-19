# Import des bibliothèques
from fastapi import FastAPI
import uvicorn
import joblib
import pandas as pd
from pydantic import BaseModel



# Création de l'instance
app = FastAPI()

# Décorateur get() qui permet de spécifier le chemin URL et l'action get (lire le texte affiché)
@app.get("/")
def welcome():
    return {"message": "Bienvenue dans notre API de prédiction"}

# BaseModel 

class Inputs(BaseModel):
    time_in_hospital : int
    num_lab_procedures : int
    num_procedures : int
    num_medications : int
    number_outpatient : int
    number_emergency :int
    number_inpatient : int
    number_diagnoses : int
    age : int

# Chemin de l'Api pour la prediction en fonction des inputs client

@app.post("/prediction")
def predict(data:Inputs):
    data_dict = data.dict()
    data_df = pd.DataFrame.from_dict([data_dict])
    model_joblib = joblib.load('model_joblib')    
    prediction = model_joblib.predict(data_df)
    return {'Oui' if prediction == 1 else 'Non'}

# @app.post("/prediction")
# def predict(data:Inputs):
#     data_dict = data.dict()
#     data_df = pd.DataFrame.from_dict([data_dict])
#     model_joblib = joblib.load('model_joblib')    
#     prediction = model_joblib.predict(data_df)
#     prediction_label = ['Oui' if prediction == 1 else 'Non']
#     return {'prediction' : prediction_label}


# Décorateur post qui permet de créer de la donnée (grâce à l'input de l'api)
# @app.post("/prediction/time_in_hospital={time_in_hospital}/num_lab_procedures={num_lab_procedures}/num_procedures={num_procedures}/num_medications={num_medications}/number_outpatient={number_outpatient}/number_emergency:{number_emergency}/number_inpatient:{number_inpatient}/number_diagnoses={number_diagnoses}/ age={age}")
# async def predict(time_in_hospital, num_lab_procedures, num_procedures, num_medications, number_outpatient, number_emergency, number_inpatient, number_diagnoses, age):

#     data = [[time_in_hospital, num_lab_procedures, num_procedures, num_medications, number_outpatient, number_emergency,
#            number_inpatient, number_diagnoses, int(age)]]
#     data = pd.DataFrame(data, columns = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
#                                          'num_medications', 'number_outpatient', 'number_emergency',
#                                            'number_inpatient', 'number_diagnoses', 'age'])
    
#     model_joblib = joblib.load('model_joblib')    
#     prediction = model_joblib.predict(data)

#     return {'Ce patient sera-t-il réhospitalisé?': 'Oui' if prediction == 1 else 'Non'}


# Pour régler erreur 404 (127.0.0.1:50629 - "GET / HTTP/1.1" 404 Not Found)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1:", port=8000)
    # uvicorn.run(app, host="0.0.0.0:", port=8000) 




# Notes 

# Problème erreur 422 dans lancement de l'API => voir pourquoi ? Ne semble pas bloquant pour le moment mais à régler : 
# https://stackoverflow.com/questions/64019054/fastapi-service-results-in-404-when-service-is-started-using-uvicorn-run


# Ajout de cette méthode pour gérer l'erreur d'accessibilité 'access-control-allow-origin' 
# from fastapi.middleware.cors import CORSMiddleware 
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )