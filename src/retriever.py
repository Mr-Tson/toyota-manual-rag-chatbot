import os
import requests
import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import SKLearnVectorStore

# Suppress warning
import warnings

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TOKENIZERS_PARALLELISM'] = "false"

def build_vector_store(content):
    # retrieving the vector store
    if content:
        if not st.session_state.vector_store:

            with st.spinner(text=":red[Pleaae wait while we fetch the information...]"):

                # fetch the embedding model
                embedding_model = HuggingFaceEmbeddings()
                # fetch the preprocessed embedding file
                embedding_file = 'https://raw.githubusercontent.com/Samuelchazy/Educative.io/8f0e764c1b69e2d61f4e44e3084c0695d85cd6e8/persistence/user_manuel.json'

                # Download the embedding file from the url and save it temporarily
                with NamedTemporaryFile(delete=False, suffix=".json") as tmp_file:
                    response = requests.get(embedding_file)
                    tmp_file.write(response.content)
                    tmp_file_path = tmp_file.name

                vector_store = SKLearnVectorStore(
                    embedding=embedding_model,
                    persist_path=tmp_file_path,
                    serializer="json",
                )

                # Save the vector store to the session state
                st.session_state.vector_store = vector_store
                return vector_store
        else:
            return st.session_state.vector_store
        
    else:
        st.error("No content was found...")

def retrieve_chunks_from_vector_store(vector_store, re_written_query):
    # retrieving the 5 most relevant chunks from the vectore store
    with st.spinner(text=":red[Please wait while we fetch the relevant information...]"):
        relevant_docs = vector_store.similarity_search_with_score(query=re_written_query, k=5)
        return relevant_docs

def retrieve_history():
    # retrieve all chat messages in the history
    for message in st.session_state.messages:
        with st.container(border=True):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
