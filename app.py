import streamlit as st
import openai

st.title("Mini DeepSeek Clone")

# L'utilisateur entre sa clé API
user_api_key = st.text_input("🔑 Enter your OpenAI API Key", type="password")

# Champ pour poser une question
user_input = st.text_input("💬 Pose ta question :")

# Bouton pour envoyer la question
if st.button("Envoyer") and user_input:
    if not user_api_key:
        st.error("⚠️ Please enter your OpenAI API Key above.")
    else:
        openai.api_key = user_api_key
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150
            )
            st.write(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

