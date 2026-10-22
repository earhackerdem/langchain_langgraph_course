from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
import streamlit as st

# Configurar la pagina de la app

st.set_page_config(page_title="ChatBot Básico", page_icon="😎")
st.title('ChatBot Básico con LangChain')
st.markdown('Este es un chatbot de ejemplo construido con LangChain + StreamLit. Escribe tu mensaje abajo para comenzar!')


with st.sidebar:
    st.header("Configuración")
    temperature = st.slider('Temperatura', 0.0, 1.0, 0.5,0.1)
    model_name = st.selectbox('Modelo',["gpt-3.5-turbo",'gpt-4',"gpt-4o-mini"])
    
    personalidad = st.selectbox(
        "Personalidad del Asistente",
        [
            "Util y amigable",
            "Profesional y formal",
            "Casual y relajado",
            "Experto tecnico",
            "Creativo y divertido"
        ]
        
    )

chat_model = ChatOpenAI(model=model_name, temperature=temperature)

system_messages = {
                "Util y amigable":"Eres un asistente útil y amigable llamado ChatBot Pro. Responde de manera clara y concisa.",
                "Profesional y formal":"Eres un asistente profesional y formal. Proporciona respuestas precisas y bien estructuradas.",
                "Casual y relajado":"Eres un asistente casual y relajado. Habla de forma natural y amigable, como un buen amigo.",
                "Experto tecnico":"Eres un asistente experto técnico. Proporciona respuestas detalladas con precisión técnica.",
                "Creativo y divertido":"Eres un asistente creativo y divertido. Usa analogías, ejemplos creativos y mantén un tono alegre."
}

prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_messages[personalidad]),
    ("human","Historial de conversacion:\n {historial}\n\nPregunta actual: {mensaje}")
])

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
   


