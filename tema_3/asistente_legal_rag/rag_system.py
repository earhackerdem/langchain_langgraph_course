from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
import streamlit as st

from config import *

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