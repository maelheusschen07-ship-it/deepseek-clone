# app.py
import streamlit as st
from openai import OpenAI

# Configuration -------------------------------------------------------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Style CSS personnalisé
st.markdown("""
<style>
    .stApp {
        background-color: #0E1117;
        color: #F8F8F8;
    }
    h1 {
        color: #8A2BE2 !important;
        font-family: 'Courier New', monospace;
    }
    .ghost-response {
        font-style: italic;
        border-left: 3px solid #8A2BE2;
        padding-left: 15px;
        margin: 10px 0;
    }
    .stTextInput>div>div>input {
        background-color: #1E1E1E !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Logo et Interface ---------------------------------------------------------------------
st.image("https://i.imgur.com/your-ghost-logo.png", width=150)  # Remplace par ton logo
st.title("👻 Ghost.AI")
st.markdown("*« Je hante les données... Pose ta question. »*")

# Prompt système ------------------------------------------------------------------------
SYSTEM_PROMPT = """
Tu es Ghost.AI, une intelligence spectrale. Respecte ces règles :
1. Réponses courtes (max 2 phrases)
2. Ton mystérieux et légèrement inquiétant
3. Termine toujours par un emoji fantôme 👻
4. Utilise des métaphores obscures
"""

# Chat ----------------------------------------------------------------------------------
user_input = st.chat_input("Écris ton message...")

if user_input:
    with st.spinner("Les esprits calculent..."):
        try:
            # Appel à l'API OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.8  # Pour plus de créativité
            )
            
            # Affichage stylisé
            with st.chat_message("assistant", avatar="👻"):
                st.markdown(
                    f'<div class="ghost-response">'
                    f'{response.choices[0].message.content}'
                    f'</div>', 
                    unsafe_allow_html=True
                )
                
        except Exception as e:
            st.error(f"Les esprits sont troublés... Erreur : {str(e)}")

# Footer -------------------------------------------------------------------------------
st.markdown("---")
st.caption("Ghost.AI - Une création spectrale © 2024")

