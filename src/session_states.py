import streamlit as st

def initialize_params():
    # initialize the session states
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    if 'vector_store' not in st.session_state:
        st.session_state.vector_store = None

