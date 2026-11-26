# Model Configuration 
EMBEDDING_MODEL = 'text-embedding-3-large'
QUERY_MODEL = 'gpt-4o-mini'
GENERATION_MODEL = 'gpt-4o'

# Vector Store Configuration
CHROMA_DB_PATH = '/Users/sehnhack/projects/personal/udemy/curso_llaipython/tema_3/chroma_db'

# Retriever Configuration
SEARCH_TYPE = "mmr"
MMR_DIVERSITY_LAMBDA = 0.7
MMR_FETCH_K = 20
SEARCH_K = 2

#Configuracion alternativa para retriever hibrido
ENABLE_HYBRID_SEARCH = True
SIMILARITY_THRESHOLD = 0.75