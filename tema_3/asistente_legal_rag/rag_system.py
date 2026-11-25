from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
import streamlit as st

from config import *
from prompts import *

def initialize_rag_system():
    
    ## Vector Store
    vector_store = Chroma(
        embedding_function=OpenAIEmbeddings(model=EMBEDDING_MODEL),
        persist_directory=CHROMA_DB_PATH
    )
    
    # Modelos
    
    llm_queries = ChatOpenAI(model=QUERY_MODEL,temperature=0)
    llm_generation = ChatOpenAI(model=GENERATION_MODEL,temperature=0)
    
    # Retriever MMR(Maximal Margin Relevance)
    
    base_retriever = vector_store.as_retriever(
        search_type = SEARCH_TYPE,
        search_kwargs = {
            "k": SEARCH_K,
            "fetch_k": MMR_FETCH_K
        }
    )
    
    #Prompt personalizado para el MultiqueryRetriever
    multi_query_prompt = PromptTemplate.from_template(MULTI_QUERY_PROMPT)

    # MultiqueryRetriever con prompt personalizado

    mmr_multi_retriever = MultiQueryRetriever.from_llm(
        retriever=base_retriever,
        llm=llm_queries,
        prompt=multi_query_prompt
    )

    prompt = PromptTemplate.from_template(RAG_TEMPLATE)