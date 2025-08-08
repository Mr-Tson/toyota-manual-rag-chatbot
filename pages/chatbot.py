import streamlit as st
from src.load_file import upload_pdf_file

# Load the user manual given by the user
user_manual_content = upload_pdf_file()

if user_manual_content:
    for page in user_manual_content:
        if page != "...":
            st.write(page)
            break
