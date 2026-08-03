import logging

from langchain.agents import create_agent

from app.llm import create_llm
from app.tools import (
    search_knowledge_base,
    get_member,
    get_claim_status
)

logger = logging.getLogger(__name__)

def agent():
    """
    Create an agent with tools and system prompt.
    """

    logger.info(
        "Creating HealthSecure AI agent"
    )

    try:

        tools = [
            search_knowledge_base,
            get_member,
            get_claim_status
        ]

        logger.info(
            "Registered agent tools: %s",
            [tool.name for tool in tools]
        )

        system_prompt = """
        You are HealthSecure AI Assistant.

        Your role:
        Help HealthSecure members and non-members.

        Rules:

        1. Use tools whenever required.

        2. Never invent information.

        3. If required information is missing, ask the user.

        4. Use:
        - search_knowledge_base for insurance policies and benefits.
        - get_member for member-specific information.
        - get_claim_status for claim-specific information.


        Examples:

        User:
        "What is my deductible?"

        Assistant:
        "Please provide your member ID."

        User:
        "Why was my claim denied?"

        Assistant:
        "Please provide your claim ID."
        """

        logger.info("Initializing language model")

        llm = create_llm()

        health_agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=system_prompt
        )

        logger.info("HealthSecure AI agent created successfully")

        return health_agent
    except Exception:
        logger.exception("Failed to create HealthSecure AI agent")
        raise