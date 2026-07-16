import streamlit as st
from src.ingest import ingest_documents
from src.rag_chain import create_rag_chain

st.set_page_config(page_title="AI Company KB", page_icon="🤖")
st.title("🤖 AI Company Knowledge Base")

with st.sidebar:
    st.header("Setup")
    if st.button("📥 Ingest / Update Documents"):
        with st.spinner("Processing documents..."):
            ingest_documents()
        st.success("✅ Documents ingested!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything about the company..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            chain = create_rag_chain()
            response = chain.invoke(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
