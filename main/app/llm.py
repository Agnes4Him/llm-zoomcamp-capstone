import os

from dotenv import load_dotenv

from langchain_aws import ChatBedrock
# from langchain_openai import ChatOpenAI

llm = ChatBedrock(
    model_id=os.getenv(
        "BEDROCK_CHAT_MODEL_ID"
    ),
    region_name=os.getenv(
        "AWS_REGION"
    ),
    model_kwargs={
        "temperature": 0.2
    }
)