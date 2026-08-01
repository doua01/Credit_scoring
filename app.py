import streamlit as st
import mlflow.sklearn
import numpy as np
import pandas as pd

# Charger le modèle depuis MLflow
model_uri = "runs:/95878e0209284063bc38914e7c99d5de/best_model"
model = mlflow.sklearn.load_model(model_uri)

st.title("Credit Scoring App")

# Interface utilisateur
age = st.number_input("Âge", min_value=18, max_value=100)
revenu = st.number_input("Revenu mensuel")
montant = st.number_input("Montant du crédit")
duree = st.number_input("Durée en mois")
score = st.number_input("Score crédit")
nb_prev = st.number_input("Nombre crédits précédents")
ratio = st.number_input("Ratio dette/revenu")

# Champs catégoriels avec les bonnes valeurs
statut = st.selectbox("Statut emploi", ["CDI", "CDD", "Indépendant", "Chômeur"])
education = st.selectbox("Niveau d'éducation", ["Bac", "Licence", "Master", "Doctorat"])
propriete = st.selectbox("Type de propriété", ["Locataire", "Propriétaire", "Autre"])
historique = st.selectbox("Historique crédit", ["Bon", "Excellent", "Acceptable", "Mauvais"])
objet = st.selectbox("Objet du crédit", ["Immobilier", "Automobile", "Professionnel", "Consommation"])

# Créer un DataFrame avec les colonnes attendues par le modèle
input_data = pd.DataFrame([{
    "Age": age,
    "Revenu": revenu,
    "Montant_Credit": montant,
    "Duree_Mois": duree,
    "Score_Credit": score,
    "Nb_Credits_Prec": nb_prev,
    "Ratio_Dette_Revenu": ratio,
    "Statut_Emploi": statut,
    "Niveau_Education": education,
    "Type_Propriete": propriete,
    "Historique_Credit": historique,
    "Objet_Credit": objet
}])

# Bouton de prédiction
if st.button("Prédire"):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)  # Probabilités
    
    if prediction[0] == 1:
        st.error(f"⚠️ Risque de défaut de paiement élevé (probabilité = {proba[0][1]:.2f})")
    else:
        st.success(f"✅ Client solvable (probabilité = {proba[0][0]:.2f})")
