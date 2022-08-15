from fastapi import FastAPI
import uvicorn
# from fastapi.middleware.cors import CORSMiddleware 
# import warnings
# warnings.filterwarnings("ignore")
import joblib


# Création de l'instance
app = FastAPI()


# Ajout de cette méthode pour gérer l'erreur d'accessibilité 'access-control-allow-origin'
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Décorateur @app.get() qui permet de spécifier le chemin URL et l'action http (get) - read data
@app.get("/root")
async def root():
    return {"message": "Bienvenue dans notre API de prédiction"}

@app.get("/prediction/time_in_hospital={time_in_hospital}/num_lab_procedures={num_lab_procedures}/num_procedures={num_procedures}/num_medications={num_medications}/number_outpatient={number_outpatient}/number_emergency:{number_emergency}/number_inpatient:{number_inpatient}/number_diagnoses={number_diagnoses}/ age={age}")
async def predict(time_in_hospital, num_lab_procedures, num_procedures, num_medications, number_outpatient, number_emergency, number_inpatient, number_diagnoses, age):

    data = [[time_in_hospital, num_lab_procedures, num_procedures, num_medications, number_outpatient, number_emergency,
           number_inpatient, number_diagnoses, int(age)]]
    data = pd.DataFrame(data, columns = ['time_in_hospital', 'num_lab_procedures', 'num_procedures',
                                         'num_medications', 'number_outpatient', 'number_emergency',
                                           'number_inpatient', 'number_diagnoses', 'age'])
    
    model_joblib = joblib.load('model_joblib')    
    prediction = model_joblib.predict(data)

    return prediction




    
# Pour régler erreur 404 (127.0.0.1:50629 - "GET / HTTP/1.1" 404 Not Found)
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)