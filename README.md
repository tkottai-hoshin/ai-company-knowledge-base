Purpose:

Most organizations have important Documents, PDFs and Information which employees need to analyze. This is an application that will help employees swift through important 'Knowledge' that lives in the organization, by using an intelligent RAG (Retrieval Augmented Generation) architecture hosted on your private cloud or local machine. 

Model Optimization: 

For larger workload, especially at the data center level, Kimi K3 is a brand new model that is compatible for Commercial / Federal / Soveriegn cloud level of process retry logic, fallback chains, output parsers, repair loops, and evaluation gates for running millions of workloads on a continuous 24/7 basis. 

For this project, running on a local machine, your limitation is your PC or Laptop. I've used Ollama which is open source model that is comparable to OpenAI, Anthropic and Kimi K3. From a data semantics perspective, were using Langchain to parse the data into different embeddings that help us store these chunks of data into a vectorization database (chroma).  

Token Optimization:

To optimize the efficiency of spending on tokens, it's important to give as much context as possible when constructing an INPUT. The Input is not only the Prompt, but it is the contextual data that the LLM is processing along with your prompt. Do ensure the correct data provided in the INPUT. 

Poor context = hallucinations or wasted tokens. 
Wasted tokens = Poor OUTPUT



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

