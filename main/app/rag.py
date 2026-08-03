import logging

from app.rag_helper import (
    create_vectorstore,
    create_retriever
)

logger = logging.getLogger(__name__)

def retrieve_documents(question):
    """
    Retrieve documents from the vectorstore
    """

    logger.info(
        "Starting document retrieval"
    )

    try:
        vectorstore = create_vectorstore()
        retriever = create_retriever(
            vectorstore
        )

        docs = retriever.get_relevant_documents(
            question
        )

        logger.info(
            "Retrieved %s relevant documents",
            len(docs)
        )

        return docs
    except Exception:
        logger.exception(
            "Failed to retrieve documents"
        )
        raise

if __name__ == "__main__":
    question = "What benefits are included?"
    docs = retrieve_documents(question)
    for doc in docs:
        print(doc.page_content)