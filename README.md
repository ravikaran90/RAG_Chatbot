Building a Chatbot with RAG (Retrieval Augmented Generation)

Process:
- Ingesting a PDF File (Anything could be ingested - File, Website etc.)
- Split the PDF file into blocks of 300 characters
- Create the embeddings of those blocks
- Store the Embeddings into a database

When a query is asked to the Chatbot, it will create the embeddings of the question and search it with the embeddings present in the database only to search the relevant blocks
