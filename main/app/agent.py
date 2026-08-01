from langchain.agents import create_agent

from langchain_core.prompts import ChatPromptTemplate

from app.llm import llm
from app.tools import (
    search_knowledge_base,
    get_member,
    get_claim_status
)

tools=[
    search_knowledge_base,
    get_member,
    get_claim_status
]

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

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)