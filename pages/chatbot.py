import streamlit as st
from src.load_file import load_file

from dotenv import load_dotenv

load_dotenv()

# Load the user manual given by the user
user_manual_content = load_file()
