from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("/Users/sehnhack/projects/personal/udemy/curso_llaipython/tema_3/saul_perez_2026.pdf")

pages = loader.load()

for i, page in enumerate(pages):
    print(f"=== Pagina {i+1}==")
    print(f"Contenido: {page.page_content}")
    print(f"Metadatos: {page.metadata}")