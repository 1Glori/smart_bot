import streamlit as st 
import os
from mistralai import Mistral

# Étape 4 : Créer une fonction pour générer des réponses
def generate_response(user_input):
    api_key = "CkFJhCJL8eDbWBx9Wh9WAJ7u7RtlTj1L"
    model = "mistral-large-latest"

    client = Mistral(api_key=api_key)

    # Appel à l'API pour obtenir une réponse à partir du modèle
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "user",
                "content": user_input(), 
            },
        ]
    )

    return chat_response.choices[0].message.content


# Configuration de l'interface Streamlit
st.title("Chatbot avec Streamlit")
st.write("Bienvenue sur l'interface de chatbot. Posez-moi des questions !")

# Initialisation de l'historique de conversation
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Étape 7 : Créer un formulaire pour saisir la question
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("Vous :", key="input", placeholder="Posez votre question ici...")
    submit_button = st.form_submit_button(label='Envoyer')

# Étape 8 : Afficher la réponse du bot
if submit_button and user_input:
    response = generate_response(user_input)  # Appeler la fonction de génération de réponse

    # Ajouter l'entrée utilisateur et la réponse à l'historique
    st.session_state.chat_history.append(("Vous", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Étape 9 : Afficher l'historique des messages
st.write("Historique des échanges :")
for sender, message in st.session_state.chat_history:
    if sender == "Vous":
        st.write(f"**{sender}:** {message}")
    else:
        st.write(f"*{sender}:* {message}")
