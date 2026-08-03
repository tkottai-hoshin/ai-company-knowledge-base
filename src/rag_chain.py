from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def create_rag_chain():
    vectorstore = Chroma(
        persist_directory="./vectorstore",
        embedding_function=OllamaEmbeddings(model="nomic-embed-text")
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    
    template = """You are a helpful AI knowledge base assistant.
Answer the question based only on the provided context.
If you don't know the answer, say "I don't have enough information in the documents."

Context: {context}

Question: {question}
"""
    
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOllama(model="llama3.2", temperature=0.3)
    
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    return rag_chain
