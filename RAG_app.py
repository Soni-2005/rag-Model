import streamlit as st
from dotenv import load_dotenv
import as
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterSplitter
from lanchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.webstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
import time

#load environment variables
load_dotenv()

#set up Groq API key
#groq_api_key=os.getenv("GROQ_API_KEY")
groq_api_key=os.getenv("GROQ_API_KEY")
st.set_page_config(page_title="Dynamic RAG with Groq", layout="wide")
st.image("aiwebproject_dp")
st.title("Dynamic RAG with Groq, FAISS, and Llama3")

#Initialize session state for vector store and chat history
if "vector" not in st.sessiom_state:
  st.session_state.vector= None
if "chat_histort" not in st.session_state:
  st.session_state.chat_history=[]

# Sidebar for document upload
with st.debar:
  
  

