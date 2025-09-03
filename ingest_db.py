from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTExtSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4

from dotenv import load_dotenv
load_dotenv()

DATA_PATH=r"data"
CHROMA_PATH=r"chroma_db"

#Initiating the Embeddings Model
embeddings_model=OpenAIEmbeddings(model="text-embedding-3-large")

#Initiate the Vector Store
vector_store=Chroma(
  collection_name="example_collection",
  embedding_function=embeddings_model,
  persist_directory=CHROMA_PATH,
)

#Loading the PDF Document
loader=PyPDFDirectoryLoader(DATA_PATH)

raw_documents=loader.load()
