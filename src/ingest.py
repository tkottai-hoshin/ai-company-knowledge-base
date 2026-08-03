from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import os

def ingest_documents():
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Please put PDF files in the data/ folder")
        return

    loader = PyPDFDirectoryLoader("data/")
    docs = loader.load()

    if not docs:
        print("No PDFs found in data/ folder")
        return

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        persist_directory="./vectorstore"
    )
    
    print(f"✅ Successfully ingested {len(splits)} chunks!")
    
if __name__ == "__main__":
    ingest_documents()
