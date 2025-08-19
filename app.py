# app.py
import streamlit as st
from openai import OpenAI

# Configuration de l'API OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Interface Streamlit
import streamlit as st

st.title("👻 Ghost.AI")  # 👈 Change ici le nom
st.markdown("*L'IA mystérieuse qui lit entre les lignes...*")  # Sous-titre optionnel

if user_input:
    # Appel à l'API OpenAI
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    
    # Affichage de la réponse
    st.write("Réponse de l'IA :")
    st.write(response.choices[0].message.content)

