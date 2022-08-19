# from http.client import _DataType
import streamlit as st
import pandas as pd
import requests
import json


# Pour la factorisation du code, voir : https://www.udemy.com/course/practical-machine-learning-for-beginner-in-2022s-in/learn/lecture/30675904#overview

st.set_page_config(layout="centered") #  "centered" or wide

tab1, tab2, tab3 = st.tabs(["Prédiction", "Mon historique de prédictions", "Mes identifiants"])

with tab1: # inputs et prédiction
    st.image('./image_rognee.jpg')
    st.subheader("Mon patient va-t-il être réhospitalisé ?")  

    col1, col2 = st.columns([3, 2], gap = 'large')
    with col1: # Questionnaire        
        with st.expander("Répondez aux questions suivantes", expanded = False):
            age = st.slider('Quel âge a votre patient', 1, 99)
            time_in_hospital = st.number_input("Combien de jours le patient a-t-il été hospitalisé ?", min_value = 1, max_value = 30)
            num_lab_procedures = st.number_input("Combien d'analyses médicales ont été faites pendant son hospitalisation ?", min_value = 0, max_value = 1000)
            num_procedures = st.number_input("Combien le patient a-t-il eu d'intervenions médicales pendant son hospitalisation ?", min_value = 0, max_value = 1000)
            num_medications = st.number_input("Combien de médicaments ont-ils été administrés au patient pendant le rdv ?", min_value = 0, max_value = 1000)
            number_outpatient = st.number_input("Combien de visites ambulatoires le patient a-t-il eu l'année précédant la consultation (en consultation externe) ?", min_value = 0, max_value = 1000)
            number_emergency = st.number_input("Combien de visites aux urgences le patient a-t-il eu l'année précédant la consultation", min_value = 0, max_value = 1000)
            number_inpatient = st.number_input("Combien de visites hospitalières le patient a-t-il eu l'année précédant la consultation", min_value = 0, max_value = 1000)
            number_diagnoses = st.number_input("Quel est le nombre de diagnostics déclarés dans le système", min_value = 0, max_value = 1000)
            
    with col2: # Output de prediction
        data_dict = {
            'time_in_hospital': time_in_hospital,
            'num_lab_procedures': num_lab_procedures,
            'num_procedures': num_procedures,
            'num_medications' : num_medications,
            'number_outpatient': number_outpatient,
            'number_emergency' : number_emergency,
            'number_inpatient': number_inpatient,
            'number_diagnoses' : number_diagnoses,
            'age' : age
            }
        if st.button("Validez vos réponses"):
            response = requests.post("http://127.0.0.1:8000/prediction", json=data_dict)
            prediction = response.text
            if prediction == 'Oui':
                # st.success('Le patient va être réhospitalisé', icon = " ")
                st.write('Le patient va être réhospitalisé')
            else:
                # st.success('Le patient ne va pas être réhospitalisé', icon =" ✅")
                st.write('Le patient ne va pas être réhospitalisé')
       
with tab2: # Récapitulatif de tous les patients 

    st.subheader("Voici le récapitulatif de vos patients :")
    st.write(pd.DataFrame(columns=['time_in_hospital', 'num_lab_procedures', 'num_procedures',
                                            'num_medications', 'number_outpatient', 'number_emergency',
                                            'number_inpatient', 'number_diagnoses', 'age', 'prediction']))

with tab3: # Identifiants du patient
    st.subheader("Indiquer les paramètres de comptes du médecin - voir si nécessaire")



#######################
# NOTES
#######################

# Personnaliser le font avec un import json ? Voir si possible ou avec des balises html/css
# To compose your own widget with ython : https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/ 
# Pour la variable age : envisager de faire un input avec des classes si on garde les catégories dans le df de base


######################
# RECAPITULATIF
#####################

# Récapitulatif (voir sous quelle forme l'indiquer sur la page web)
        
        # st.subheader("Récapitulatif")
        # st.markdown(
        #         f"""
        #         *Age : {age}  
        #         *Temps d'hospitalisation* : {time_in_hospital}  
        #         *Nombre d'analyses médicales* : {num_lab_procedures}  
        #         *Nombre d'interventions médicales* : {num_procedures}  
        #         *Nombre de médicaments prescrits* : {num_medications}  
        #         *Nombre de visites en consultation externe* : {number_outpatient}  
        #         *Nombre de visites aux urgences* : {number_emergency}  
        #         *Nombre de visites hospitalières* : {number_inpatient}  
        #         *Nombre de diagnostics* : {number_diagnoses}  
        #         """
        #         )
        
        # recap = {'Temps hospitalisation':time_in_hospital,
        #         'Nombre analyses médicales':num_lab_procedures,
        #         'Nombre interventions médicales' : num_procedures,
        #         'Nombre médicaments prescrits': num_medications,
        #         'Nombre visites consult ext' : number_outpatient,
        #         'Nombre visites urgences' : number_emergency,  
        #         'Nombre visites hospitalières' : number_inpatient,  
        #         'Nombre diagnostics' : number_diagnoses  
        #          }
        # st.write(pd.DataFrame(data = recap, index=[0]))
    