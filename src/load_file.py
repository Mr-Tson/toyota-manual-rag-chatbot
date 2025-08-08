import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader


def upload_pdf_file():

    # upload pdf file
    uploaded_pdf_file = st.file_uploader("Upload your .pdf file", type="pdf")

    if uploaded_pdf_file:

        # Create a temporary file and write data of pdf to temp-file
        with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_pdf_file.getbuffer())
            temp_file_path = temp_file.name

        # Load pdf content using PyPDFLoader
        pdf_loader = PyPDFLoader(temp_file_path)
        pdf_reader = pdf_loader.load()

        # Extract and format the content
        content = [(page.page_content.replace("\n", "\n\n") if page.page_content else '...') for page in pdf_reader]

        return content


