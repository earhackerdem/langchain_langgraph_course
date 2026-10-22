from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt = ChatPromptTemplate.from_messages([
    ("system","Eres un asistente util que mantiene el contexto de la conversacion"),
    MessagesPlaceholder(variable_name="historial"),
    ("human","{pregunta_actual}")
    
])

#Simulamos un historial de conversacion
historial_conversacion = [
    HumanMessage(content="Cual es la capital de Francia"),
    AIMessage(content="La capital de Paris es Francia"),
    HumanMessage(content="Y cuantos habitantes tiene?"),
    AIMessage(content="París tiene aproximadamente 2.2 Millones de habitantes en la ciudad"),
]

mensajes = chat_prompt.format_messages(
    historial=historial_conversacion,
    pregunta_actual = "Puedes decirme algo interesante de su arquitectura?"
)

for m in mensajes:
    print(m.content)