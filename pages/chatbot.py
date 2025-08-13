import streamlit as st
from src.generator import generate_answer
from src.load_file import load_file
from src.retriever import build_vector_store, retrieve_history, retrieve_chunks_from_vector_store
from src.rewrite_query import rewrite_user_query

from dotenv import load_dotenv

load_dotenv()

# Load the user manual given by the user
user_manual_content = load_file()

# If load is successful
if user_manual_content:
    try:
        # display the title
        st.title(":rainbow[TOYOTA HIGHLANDER INTERACTIVE BOT]")
        st.write('')

        # set a clear conversation button on the side menu
        clear_conversation = st.sidebar.button(label='Clear conversation',
                                               key='clear_conversation',
                                               use_container_width=True)

        if clear_conversation:
            st.session_state.messages = []

        # display the chatbot input space
        user_input = st.chat_input(
            'Ask me a question about the Toyota Highlander...',
            max_chars=1500,
            key='user_input',
        )

        # build the vector store
        vector_store = build_vector_store(user_manual_content)

        # display the chat history
        chat_history = retrieve_history()

        if user_input:
            # append the user input to the chat
            st.session_state.messages.append({'role':'user', 'content': user_input})
            # rewrite the query for better input to the llm
            rewritten_user_query = rewrite_user_query(user_input)
            # retrieve the relevant chunks from the database
            relevant_chunks = retrieve_chunks_from_vector_store(vector_store, rewritten_user_query)
            # generate a final answer using the llm
            all_results = generate_answer(rewritten_user_query, relevant_chunks)
            # display the answer with the relevant information in 2 cols, left col writes rewritten query, right col writes rel_chunks
            col_left, col_right = st.columns(2)
            with col_left:
                with st.expander(label='Rewritten user query', expanded=False):
                    st.write(rewritten_user_query)  
            with col_right:
                with st.expander(label="Retrieved relevant text from the car user manual", expanded=False):
                    st.write(relevant_chunks)

    # handle the exception
    except Exception as e:
        print(e)
        print("Sorry, there was an error.")
