from langchain_openai import ChatOpenAI
from models.cv_model import AnalisisCV
from prompts.cv_prompts import crear_system_prompts

def crear_evaluador_cvs():
    modelo_base = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    modelo_estructurado = modelo_base.with_structured_output(AnalisisCV)
    chat_prompt = crear_system_prompts()
    cadena_evaluacion = chat_prompt | modelo_estructurado
    
    return cadena_evaluacion

def evaluar_candidato(texto_cv: str, descripcion_puesto:str) -> AnalisisCV:
    try:
        cadena_evaluacion = crear_evaluador_cvs()
        resultado = cadena_evaluacion.invoke({
            "texto_cv":texto_cv,
            "descripcion_puesto": descripcion_puesto 
        })
        
        return resultado
    except Exception as e:
        return AnalisisCV(
            nombre_candidato="Error en procesamiento",
            experiencia_años=0,
            habilidades_clave=["Error al procesar cv"],
            education='No se puede determinar',
            experiencia_relevante="Error durante el analisis",
            fortalezas=["requiere revision manual del cv"],
            areas_mejora=["verificar formato del pdf"],
            porcentaje_ajuste=0
        )
    