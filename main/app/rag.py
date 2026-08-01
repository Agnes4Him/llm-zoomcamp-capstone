import os

from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

from langchain_aws import BedrockEmbeddings

load_dotenv()

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

embeddings = BedrockEmbeddings( 
    model_id=os.getenv(
        "BEDROCK_EMBEDDING_MODEL_ID"
    ),
    region_name=os.getenv(
        "AWS_REGION"
    )
)

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={
        "k":3
    }
)