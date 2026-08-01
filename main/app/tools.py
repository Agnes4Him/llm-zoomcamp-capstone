from langchain_core.tools import tool

from app.rag import retriever
from app.database import engine

@tool("search_knowledge_base")
def search_knowledge_base(
    question:str
):
    """
    Search HealthSecure policy documents.
    """

    docs = retriever.invoke(
        question
    )


    return "\n\n".join(
        [
            d.page_content
            for d in docs
        ]
    )

@tool
def get_member(member_id: int) -> str:
    """
    Retrieve member information using member_id.
    member_id is required and must be an integer.
    """

    if not member_id:
        return "Member ID is required."

    try:
        member_id = int(member_id)
    except ValueError:
        return "Member ID must be a number."

    sql = """
    SELECT *
    FROM members
    WHERE member_id=:id
    """

    with engine.connect() as conn:
        result = conn.execute(
            text(sql),
            {
                "id": member_id
            }
        )

        row = result.fetchone()
    if row:
        return str(dict(row._mapping))

    return "Member not found"

@tool
def get_claim_status(claim_id: str) -> dict:
    """
    Retrieve claim status using a claim ID.
    """

    sql = """
    SELECT *
    FROM claims
    WHERE claim_id = :id
    """

    with engine.connect() as conn:
        result = conn.execute(
            text(sql),
            {
                "id": claim_id
            }
        )

        row = result.fetchone()

    if not row:
        return {
            "message": "Claim not found"
        }

    return dict(row._mapping)