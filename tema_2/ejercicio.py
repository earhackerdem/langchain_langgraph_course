from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
import json

llm = ChatOpenAI(model='gpt-4o-mini', temperature=0)

def preprocess_text(text):
    """Limpia el texto eliminado espacios extras y limitando longitud"""
    text = text.strip()
    return text[:500]

def generate_summary(text):
    """Genera un resumen conciso del texto"""
    prompt = f"Resume en una sola oración: {text}"
    response = llm.invoke(prompt)
    return response.content

def analyze_sentiment(text):
    """Analiza el sentimiento y devuelve resultado estructurado"""
    prompt = f"""Analiza el sentimiento del siguiente texto.
     Responde ÚNICAMENTE en formato JSON válido:
     {{"sentimiento":"positivo|negativo|neutro", "razon":"justificacion breve"}}
     
     Texto: {text} 
    """
    
    response = llm.invoke(prompt)
    
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"sentimiento":"neutro","razon":"Error en análisis"}
    
def merge_results(data):
    """Combina los resultados de ambas ramas en un formato unificado"""
    return {
        "resumen": data["resumen"],
        "sentimiento": data["sentimiento_data"]["sentimiento"],
        "razon": data["sentimiento_data"]["razon"]
    }
    
def process_one(t):
    resumen = generate_summary(t)
    sentimiento_data = analyze_sentiment(t)
    return merge_results({
        "resumen": resumen,
        "sentimiento_data": sentimiento_data
    })
    
process = RunnableLambda(process_one)
    
chain = preprocess_text | process

textos_prueba = [
    "Me encanta este producto! Funciona perfectamente y llego muy rapido",
    "El servicio al cliente fue terrible, nadie me ayudo con mi problema",
    "El clima esta nublado hoy, probablemente llueva mas tarde"
]

for texto in textos_prueba:
    resultado = chain.invoke(texto)
    print(f"Texto: {texto}")
    print(f"Resultado: {resultado}")
    print("-" * 50)