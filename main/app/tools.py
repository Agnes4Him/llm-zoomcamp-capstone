import logging

from langchain_core.tools import tool
from sqlalchemy import text

from app.rag_helper import create_vectorstore, create_retriever
from app.database import engine

logger = logging.getLogger(__name__)

@tool
def search_knowledge_base(
    question: str
):
    """
    Search HealthSecure policy documents.
    """

    logger.info(
        "Searching knowledge base"
    )

    try:
        vectorstore = create_vectorstore()
        retriever = create_retriever(vectorstore)

        docs = retriever.invoke(
            question
        )

        logger.info(
            "Knowledge base search completed. Documents retrieved: %s",
            len(docs)
        )

        return "\n\n".join(
            [
                d.page_content
                for d in docs
            ]
        )

    except Exception:
        logger.exception("Knowledge base search failed")
        raise


@tool
def get_member(member_id: int) -> str:
    """
    Retrieve member information using member_id.
    member_id is required and must be an integer.
    """

    logger.info("Retrieving member information")

    if not member_id:
        logger.warning("Member lookup attempted without member ID")
        return "Member ID is required."

    try:
        member_id = int(member_id)

    except ValueError:
        logger.warning("Invalid member ID format")

        return "Member ID must be a number."

    sql = """
    SELECT *
    FROM members
    WHERE member_id=:id
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(sql),
                {
                    "id": member_id
                }
            )

            row = result.fetchone()


        if row:
            logger.info("Member record found")

            return str(dict(row._mapping))

        logger.info("Member record not found")

        return "Member not found"

    except Exception:
        logger.exception("Failed to retrieve member information")
        raise

@tool
def get_claim_status(claim_id: str) -> dict:
    """
    Retrieve claim status using a claim ID.
    """

    logger.info("Retrieving claim status")

    sql = """
    SELECT *
    FROM claims
    WHERE claim_id = :id
    """

    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(sql),
                {
                    "id": claim_id
                }
            )

            row = result.fetchone()

        if not row:
            logger.info("Claim record not found")

            return {
                "message": "Claim not found"
            }

        logger.info("Claim record found")

        return dict(row._mapping)

    except Exception:
        logger.exception("Failed to retrieve claim status")
        raise