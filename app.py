from pydantic import BaseModel
from typing import Literal
import streamlit as st

import random

class Message(BaseModel):
    """ Classe para manter as mensagens"""
    origin: Literal["human","ai"]
    message: str

ai_messages = random.choice(["Olá, em que posso ajudar?", "Sim, com certeza.", "Essa é a resposta que tenho agora", "Não tenho essa informação"])

# Configurações gerais da página
st.set_page_config(page_title="ChatGPT - Operador", page_icon=":bee:")

with st.sidebar:
    st.title("ChatGPT da Operação :robot_face:")
    st.caption("Dados de 01 de Julho a 15 de Setembro de 2023.")
    with st.expander("Assuntos disponíveis:"):
        st.write("CAG / Desligamento forçado / Intervenções / Controle de Tensão")

if "history" not in st.session_state:
    st.session_state.history = []

with st.chat_message("ai"):
    st.write("Olá, no que posso te ajudar hoje? 👋")

prompt = st.chat_input("Digite sua pergunta aqui")

if prompt:
    st.session_state.history.append(Message(origin="human", message=prompt))
    st.session_state.history.append(Message(origin="ai", message=ai_messages))

chat_placeholder = st.container()

with chat_placeholder:
    for chat in st.session_state.history:
        with st.chat_message(chat.origin):
            st.write(chat.message)        