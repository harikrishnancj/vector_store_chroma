from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
from document import doc
load_dotenv()

from langchain_huggingface import HuggingFaceEndpointEmbeddings

llm = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")


#vector store
vector_store=Chroma(
    collection_name='Chroma',
    persist_directory='chroma_db',
    embedding_function=llm

)

#adding to vector store
vector_store.add_documents(documents=doc)

#viewing it

res=vector_store.get(include=['embeddings','documents', 'metadatas'])

#print(res)


