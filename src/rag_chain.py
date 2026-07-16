from dotenv import load_dotenv
load_dotenv()   # This line is the fix

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def create_rag_chain():
    vectorstore = Chroma(
        persist_directory="./vectorstore",
        embedding_function=OpenAIEmbeddings()
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    
    template = """You are a helpful assistant for an AI company.
    Answer the question based only on the provided context.
    If you don't know, say "I don't have enough information."
    
    Context: {context}
    Question: {question}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
    
    rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain
