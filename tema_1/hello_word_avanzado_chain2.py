from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


model = ChatOpenAI(model='gpt-4o-mini',temperature=0.7)

plantilla = PromptTemplate(
    input_variables = ['name'],
    template = "Saluda al usuario con su nombre\nNombre del usuario {name}\nAsistente:"
)

chain = plantilla | model

resultado = chain.invoke({'name':'Saúl'})

print(resultado.content)

