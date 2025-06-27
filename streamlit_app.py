import streamlit as st
import pandas as pd
import os

# Chemin local vers le fichier
file_path = r"C:\Users\tchauvin\Station REV\Station REV - Documents\5. Développement\Test carte.xlsx"

# Vérifie l'existence du fichier
if os.path.exists(file_path):
    st.success(f"Fichier trouvé : {file_path}")
    try:
        df = pd.read_excel(file_path)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur de lecture du fichier : {e}")
else:
    st.error(f"Fichier non trouvé au chemin : {file_path}")
