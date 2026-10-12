from langchain_openai import ChatOpenAI
from langchain_core.prompts import PrompTemplate

llm = ChatOpenAI(model='gpt-4o-mini',temperature=0.7)

plantilla = PrompTemplate(
    input_variables = ['nombre'],
    template = "Saluda al usuario con su nombre\nNombre del usuario {nombre}\nAsistente:"
)



