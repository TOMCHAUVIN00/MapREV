import streamlit as st
import pandas as pd

# Lien Dropbox direct (avec ?dl=1 à la fin)
dropbox_url = "https://www.dropbox.com/scl/fi/mtsm92eggj6uefnrkmnew/Test-carte.xlsx?rlkey=tkzi1bqb8s7wcusewt47znv0u&st=3476d3gk&dl=1"

try:
    df = pd.read_excel(dropbox_url)
    st.success("Fichier chargé depuis Dropbox.")
    st.dataframe(df)
except Exception as e:
    st.error(f"Erreur lors de la lecture du fichier : {e}")
