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
    response = client.chat.completions.create(...)
    st.write(f"**Ghost.AI** : {response.choices[0].message.content}")  # 👈 Ajoute le nom ici
    
   response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system", 
            "content": "Tu es Ghost.AI, une intelligence fantomatique. Tes réponses sont mystérieuses, concises et parfois énigmatiques. Signe toujours tes réponses par '👻'."
        },
        {"role": "user", "content": user_input}
    ]
)

