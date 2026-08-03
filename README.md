Purpose:

Most organizations have important Documents, PDFs and Information which employees need to analyze. This is an application that will help employees swift through important 'Knowledge' that lives in the organization, 
by using an intelligent RAG (Retrieval Augmented Generation) architecture hosted on your private cloud or local machine. 


Tech stack:

- LangChain
- Kimi K3 (Open source LLM)
- Streamlit (Frontend)
- Chroma (Vector Storage)
- Running on local machine


Codebase Structure: 
1) App.py: This is the frontend (Streamlit) code. It handles the chat interface and calls the other modules. 
2) Ingest.py: This file is responsible for loading PDF documents, splitting the data into chunks, creating semantic embeddings, and storing them in a vector database (Chroma).
3) rag_chain.py: Contains the RAG pipeline. When a user asks a question, it retrieves the most relevant document chunks and passes them to the LLM (Kimi K3) to generate an accurate answer.

