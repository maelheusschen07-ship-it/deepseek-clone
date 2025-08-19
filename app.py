import streamlit as st
import openai

# Titre de l'application
st.title("Mini DeepSeek Clone")

# Récupération de la clé API depuis les secrets Streamlit
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Champ de texte pour poser une question
user_input = st.text_input("Pose ta question :")

# Quand l'utilisateur clique sur le bouton
if st.button("Envoyer") and user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}],
        max_tokens=150
    )
    st.write(response['choices'][0]['message']['content'])
