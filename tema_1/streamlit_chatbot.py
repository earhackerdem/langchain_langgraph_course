from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
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


prompt_template = PromptTemplate(
    input_variables = ['mensaje', 'historial'],
    template="""Eres un asistente útil y amigable llamado ChatBot Pro.
    
    Historial de conversación:
    {historial}

    Responde de manera clara y concisa a la siguiente pregunta:

    {mensaje}
    """
)

chain =  prompt_template | chat_model



# Inicializar el historial de mensajes
if "messages" not in st.session_state:    
    historial = []
else:
    historial = st.session_state.messages
## Mostrar mensajes previos
for msg in historial:
    if isinstance(msg,SystemMessage):
        #No muestro el SystemMessage
        continue
    role = "assistant" if isinstance(msg,AIMessage) else "user"
    
    with st.chat_message(role):
        st.markdown(msg.content)

    #Cuadro de entrada de texto de usuario
pregunta = st.chat_input("Escribe tu mensaje: ")

if st.button('Nueva conversación'):
    historial = []
    st.rerun()
    

if pregunta:
        #Mostrar inmediatamente el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(pregunta)
        
    try:
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = ""
            
            #Inicio del streaming
            for chunk in chain.stream({'mensaje':pregunta,"historial":historial}):
                full_response += chunk.content
                response_placeholder.markdown(full_response + "▌")
                response_placeholder.markdown(full_response)
        
       
        # Almacenamos el mensaje en la memoria de streamlit
        historial.append(HumanMessage(content=pregunta))
        
        historial.append(AIMessage(content=full_response))
        
        st.session_state.messages = historial

    
    except Exception as e:
        st.error(f"Error al generar la respuesta: {str(e)}")
        st.info("Verifica que tu API KEY de OPENAI este configurada correctamente")


        # Mostrar la respuesta en la interfaz
   


