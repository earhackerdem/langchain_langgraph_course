from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classics.chains import LLMChain

model = ChatOpenAI(model='gpt-4o-mini',temperature=0.7)

plantilla = PromptTemplate(
    input_variables = ['nombre'],
    template = "Saluda al usuario con su nombre\nNombre del usuario {nombre}\nAsistente:"
)

chain = LLMChain(llm=model,prompt=plantilla)

resultado = chain.run(nombre="Saul")

print(resultado)

