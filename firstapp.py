import requests
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores.qdrant import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List
import streamlit as st
import tiktoken
from streamlit_chat import message
