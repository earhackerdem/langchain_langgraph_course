from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder



chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="Eres un experto en análisis de sentimientos. Clasifica cada texto como: POSITIVO, NEGATIVO o NEUTRO"),
    MessagesPlaceholder(variable_name="ejemplos"),
    ("human","Texto a analizar: {texto_usuario}")
]
)

#Simulamos un historial de conversacion
ejemplos_sentimientos = [
    HumanMessage(content="Texto a analizar: Me encanta este producto, es increíble"),
    AIMessage(content="POSITIVO"),
    HumanMessage(content="Texto a analizar: El servicio fue terrible, muy decepcionante"),
    AIMessage(content="NEGATIVO"),
    HumanMessage(content="Texto a analizar: El clima está nublado"),
    AIMessage(content="NEUTRO"),
]


mensajes = chat_prompt.format_messages(
    ejemplos = ejemplos_sentimientos,
    texto_usuario = "!Qué día tan maravilloso!"
)

for i, m in enumerate(mensajes):
    print(f"Mensaje {i+1} ({m.__class__.__name__}):")
    print(m.content)
    print("-" * 40)