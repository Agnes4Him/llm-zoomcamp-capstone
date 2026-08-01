import os

from dotenv import load_dotenv

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_aws import BedrockEmbeddings
# from langchain_openai import OpenAIEmbeddings

from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone

load_dotenv()

loader = DirectoryLoader(
    "knowledge-base",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

print(
    f"Loaded {len(documents)} documents"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)


chunks = splitter.split_documents(
    documents
)


print(
    f"Created {len(chunks)} chunks"
)

embeddings = BedrockEmbeddings( 
    model_id=os.getenv(
        "BEDROCK_EMBEDDING_MODEL_ID"
    ),
    region_name=os.getenv(
        "AWS_REGION"
    )
)

pc = Pinecone(
    api_key=os.getenv(
        "PINECONE_API_KEY"
    )
)

index = pc.Index(
    os.getenv(
        "PINECONE_INDEX_NAME_BEDROCK"
    )
)

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)


vectorstore.add_documents(
    chunks
)


print(
    "Knowledge base loaded into Pinecone"
)