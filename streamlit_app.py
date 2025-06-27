import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import os

st.title("🗺️ Carte interactive des sites (Excel local)")

# Chemin complet vers le fichier Excel
file_path = r"C:\Users\tchauvin\Station REV\Station REV - Documents\5. Développement\Test carte.xlsx"

if not os.path.exists(file_path):
    st.error(f"Fichier introuvable : {file_path}")
else:
    try:
        df = pd.read_excel(file_path) 

        required_cols = ['Nom du site', 'Latitude', 'Longitude', 'État']
        if not all(col in df.columns for col in required_cols):
            st.error(f"Le fichier doit contenir les colonnes suivantes : {required_cols}")
        else:
            color_param = st.selectbox("🎨 Choisir un paramètre pour la couleur des points", options=['État'])

            unique_values = df[color_param].unique()
            color_palette = ['green', 'orange', 'red', 'blue', 'purple', 'gray']
            color_map = {val: color_palette[i % len(color_palette)] for i, val in enumerate(unique_values)}

            center_lat = df['Latitude'].mean()
            center_lon = df['Longitude'].mean()
            m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

            for _, row in df.iterrows():
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=row['Nom du site'],
                    tooltip=f"{row['Nom du site']} - {row[color_param]}",
                    icon=folium.Icon(color=color_map.get(row[color_param], 'gray'))
                ).add_to(m)

            st.success(f"{len(df)} sites affichés sur la carte.")
            st_folium(m, width=800, height=600)

    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier : {e}")
