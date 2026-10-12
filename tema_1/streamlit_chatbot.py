from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st

# Configurar la pagina de la app

st.set_page_config(page_title="ChatBot Básico", page_icon="😎")
st.title('ChatBot Básico con LangChain')
st.markdown('Este es un chatbot de ejemplo construido con LangChain + StreamLit. Escribe tu mensaje abajo para comenzar!')


with st.sidebar:
    st.header("Configuración")
    temperature = st.slider('Temperatura', 0.0, 1.0, 0.5,0.1)
    model_name = st.selectbox('Modelo',["gpt-3.5-turbo",'gpt-4',"gpt-4o-mini"])

chat_model = ChatOpenAI(model=model_name, temperature=0.5)


# Inicializar el historial de mensajes
if "messages" not in st.session_state:    
    st.session_state.messages = []

## Mostrar mensajes previos
for msg in st.session_state.messages:
    if isinstance(msg,SystemMessage):
        #No muestro el SystemMessage
        continue
    role = "asssitant" if isinstance(msg,AIMessage) else "user"
    
    with st.chat_message(role):
        st.markdown(msg.content)

    #Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if pregunta:
        #Mostrar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)
       
        # Almacenamos el mensaje en la memoria de streamlit
    st.session_state.messages.append(HumanMessage(content=pregunta))

        # Generar respuesta usando el modelo de Lenguaje
    respuesta = chat_model.invoke(st.session_state.messages)

        # Mostrar la respuesta en la interfaz
    with st.chat_message('assistant'):
        st.markdown(respuesta.content)

    st.session_state.messages.append(respuesta)