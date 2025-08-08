import streamlit as st
from tempfile import NamedTemporaryFile
from langchain_community.document_loaders import PyPDFLoader


def upload_pdf_file(uploaded_pdf_file):

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

def load_file():
    # upload pdf file
    uploaded_pdf_file = st.file_uploader("Upload your .pdf file", type="pdf")

    # display the PDF file and the images
    with st.spinner('Loading PDF content. Please wait around a minute...'):
        content = upload_pdf_file(uploaded_pdf_file)

    if content:
        with st.container(height=600, border=False):
            col_left, col_right = st.columns(2)

            ###################################### Display the images #####################################
            with col_left:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_3.jpg"
                st.image(image_path, use_container_width=True)

                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_4.jpg"
                st.image(image_path, use_container_width=True)

            with col_right:
                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_5.jpg"
                st.image(image_path, use_container_width=True)

                image_path = "https://raw.githubusercontent.com/Samuelchazy/Educative.io/19d3100db50749489689a5c21029c3499722b254/images/Toyota_6.jpg"
                st.image(image_path, use_container_width=True)

        return content

    else:
        st.error('User Manual not found')
        return None

