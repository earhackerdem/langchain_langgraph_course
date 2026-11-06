from langchain_community.document_loaders import GoogleDriveLoader

credentials_path = "/Users/sehnhack/projects/personal/udemy/curso_llaipython/tema_3/credentials.json"
token_path = "/Users/sehnhack/projects/personal/udemy/curso_llaipython/tema_3/token.json"

loader = GoogleDriveLoader(
    folder_id="1UcNSufuRehfqmjudnAuyvhZtMdsBV58k",
    credentials_path=credentials_path,
    token_path=token_path,
    recursive=True
)

documents = loader.load()

print(f"Metadatos {documents[0].metadata}")
print(f"Contenido {documents[0].page_content}")