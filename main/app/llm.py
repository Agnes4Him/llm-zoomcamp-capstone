import os
import logging

from dotenv import load_dotenv

# from langchain_aws import ChatBedrock
from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)

load_dotenv()

def create_llm():

    chat_model = os.getenv(
        "OPENAI_CHAT_MODEL",
        "gpt-4.1-mini"
    )

    logger.info(
        "Initializing LLM with model: %s",
        chat_model
    )

    try:
        llm = ChatOpenAI(
            model=chat_model,
            temperature=0.2
        )

        logger.info(
            "LLM initialized successfully"
        )

    except Exception:
        logger.exception(
            "Failed to initialize LLM"
        )
        raise

    # Chat with Bedrock
    """
    llm = ChatBedrock(
        model_id=chat_model,
        region_name=os.getenv(
            "AWS_REGION"
        ),
        model_kwargs={
            "temperature": 0.2
        }
    )
    """

    return llm