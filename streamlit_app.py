import streamlit as st
import pandas as pd

# Remplace par ton lien de téléchargement direct généré
excel_url = "https://seeyousun-my.sharepoint.com/personal/tchauvin_seeyousun_fr/_layouts/15/download.aspx?SourceUrl=..."

try:
    df = pd.read_excel(excel_url)
    st.success("Fichier chargé depuis OneDrive/SharePoint.")
    st.dataframe(df)
except Exception as e:
    st.error(f"Erreur lors de la lecture du fichier : {e}")
