import json
import time
import streamlit as st
from api import generate

st.title('Olá, eu sou sua IA de receitas ✨')
# Criando um formulário
with st.form(key='my_form'):
    ingredientes = st.text_input('Quais ingredientes você tem disponíveis em casa?', placeholder="Exemplo: Pão, queijo, requeijão e presunto")
    tipo = st.selectbox('Qual tipo de refeição você deseja ?', ["café da manhã", "almoço", "jantar","lanche"])
    culinaria = st.text_input('Qual tipo de culinária você deseja na sua receita?', placeholder="Exemplo: italiana, japonesa, mexicana, etc.")
    # tempoPreparo = st.text_input('Qual tempo esperado você quer levar nessa receita ?', placeholder="Exemplo: 30 minutos")
    nivelUsuario = st.selectbox('Qual tipo de refeição você deseja ?', ["Iniciante", "Intermediario", "Experiente"])
    qtdPessoas = st.text_input('Essa refeição é pra quantas pessoas ?', placeholder="2")
    restricoes = st.text_input('Você possui alguma restrição ?' , placeholder="Exemplo: sem glúten, vegetariano ou baixa caloria")

    submit_button = st.form_submit_button('Enviar')

def cook_breakfast():
    msg = st.toast('Verificando os ingredientes...')
    time.sleep(1)
    msg.toast('Gerando receitas...',  icon = "🍽️")
    time.sleep(1)
    msg.toast('Resultado!', icon = "🥞")

@st.dialog("Nova Receita 😍")
def modal(item):
    st.subheader(item["titulo"])

    with st.expander("Ingredientes"):
        for ingrediente in item["ingredientes"]:
            st.markdown(f"- {ingrediente}")

    st.markdown("**Modo de Preparo:**")
    for i, instrucao in enumerate(item["modo_preparo"], 1):
        st.markdown(f"{i}. {instrucao}")
@st.dialog("Error 😒")
def show_error_modal(mensagem):
    st.error(f"Erro: {mensagem}")

if submit_button:
    resultado = generate(ingredientes, tipo, culinaria, nivelUsuario, qtdPessoas, restricoes)

    try:
        
        dados = json.loads(resultado)  
        cook_breakfast()
        if dados.get("error", False):
            show_error_modal(dados["mensagem"])
        else:
            if dados is not None:
                modal(dados)
            else:
                st.error("Nenhuma receita válida encontrada.")
            
    except json.JSONDecodeError:
        st.error("Erro ao processar a resposta. Tente novamente.")
