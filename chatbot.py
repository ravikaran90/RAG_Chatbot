from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from Langchain_chroma import Chroma
import gradio as gr

#Import the env file
from dotenv import load_dotenv
load_dotenv()

DATA_PATH=r"data"
CHROMA_PATH=r"chroma_db"

#Initiating the Embeddings Model
embeddings_model=OpenAIEmbeddings(model="text-embedding-3-large")

#Connect to ChromaDB
vector_store=Chroma(
  collection_name="example_collection",
  embedding_function=embeddings_model,
  persist_directory=CHROMA_PATH,
)

#Setup the Vector Store to be the retriever
num_results=5
retriever=vector_store.as_retriever(search_kwargs={'k':num_results})

#Call to this function for every message added to the Chatbot
def stream_response(message,history):

  #Retrieve the relevant chunks based on the questions asked
  docs=retriever.invoke(message)

  #Add all the chunks to knowledge
  knowledge=""

  for doc in docs:
    knowledge+=doc.page_content+"\n\n"

  #Make the call to the LLM (including prompt)
  if message is not None:
    partial_message=""

    rag_prompt=f"""
    An assistant which answers questions based on the knowledge which is provided to you.
    While answering, you don't use your internal knowledge, but solelyt the knowledge in the knowledge section
    You don't mention anything to the user about the provided knowledge.

    The question:{message}
    Conversation history:{history}
    The Knowledge:{knowledge}
    """
    #print(rag_prompt)

    #Stream the response to the Gradio App
    for response in llm.stream(rag_prompt)
      partial_message+=response.content
      yield partial_message
  
#Initiate the Gradio App
chatbot=gr.ChatInterface(stream_response,textbox=gr.Textbox(placeholder="Sent to the LLM...",
container=False,
autoscroll=True,
scale=7),
)

#Launch the Gradio App
chatbot.launch()
