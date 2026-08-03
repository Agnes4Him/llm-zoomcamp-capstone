import os
import logging

from dotenv import load_dotenv

# from langchain_aws import BedrockEmbeddings
from langchain_openai import OpenAIEmbeddings

from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone

logger = logging.getLogger(__name__)

load_dotenv()

def create_embeddings():
    """
    Create embeddings
    """

    logger.info("Creating embeddings model")

    try:
        openai_embedding_model = os.getenv(
            "OPENAI_EMBEDDING_MODEL"
        )

        embeddings = OpenAIEmbeddings(
            model=openai_embedding_model
        )

        logger.info(
            "Embeddings model initialized: %s",
            openai_embedding_model
        )

        return embeddings

    except Exception:
        logger.exception(
            "Failed to create embeddings model"
        )
        raise

    # bedrock_embedding_model_id = os.getenv("BEDROCK_EMBEDDING_MODEL_ID")
    """ embeddings = BedrockEmbeddings( 
        model_id=bedrock_embedding_model_id,
        region_name=os.getenv(
            "AWS_REGION"
        )
    ) """

def create_vectorstore():
    """
    Create a vectorstore in Pinecone
    """

    logger.info(
        "Creating Pinecone vectorstore"
    )

    try:
        pc = Pinecone(
            api_key=os.getenv(
                "PINECONE_API_KEY"
            )
        )

        # bedrock_index_name = os.getenv("PINECONE_INDEX_NAME_BEDROCK")
        openai_index_name = os.getenv(
            "PINECONE_INDEX_NAME_OPENAI"
        )

        logger.info(
            "Connecting to Pinecone index: %s",
            openai_index_name
        )

        index = pc.Index(openai_index_name)

        embeddings = create_embeddings()

        vectorstore = PineconeVectorStore(
            index=index,
            embedding=embeddings
        )

        logger.info(
            "Pinecone vectorstore created successfully"
        )

        return vectorstore

    except Exception:
        logger.exception("Failed to create Pinecone vectorstore")
        raise

def create_retriever(vectorstore):
    """
    Create a retriever for the vectorstore.
    """

    logger.info(
        "Creating vectorstore retriever"
    )

    try:
        retriever = vectorstore.as_retriever(
            search_kwargs={
                "k":3
            }
        )

        logger.info(
            "Retriever created successfully"
        )

        return retriever
    except Exception:
        logger.exception("Failed to create retriever")
        raise