import streamlit as st
import pandas as pd

st.title("Carte interactive avec vos points")

# Saisie des coordonnées
latitude = st.number_input("Latitude", value=48.117266)
longitude = st.number_input("Longitude", value=-1.677793)
nom = st.text_input("Nom du lieu", value="Rennes")

# Bouton pour ajouter le point
if 'points' not in st.session_state:
    st.session_state.points = pd.DataFrame(columns=['latitude', 'longitude', 'nom'])

if st.button("Ajouter le point"):
    nouveau_point = pd.DataFrame([[latitude, longitude, nom]], columns=['latitude', 'longitude', 'nom'])
    st.session_state.points = pd.concat([st.session_state.points, nouveau_point], ignore_index=True)

# Affichage de la carte
st.map(st.session_state.points[['latitude', 'longitude']])

# Affichage des points ajoutés
st.write("Points ajoutés :")
st.dataframe(st.session_state.points)
