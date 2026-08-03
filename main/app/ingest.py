import logging

from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from app.rag_helper import (
    create_vectorstore
)

logger = logging.getLogger(__name__)

def load_knowledge_base():
    """
    Load the knowledge base into Pinecone
    """

    logger.info("Loading knowledge base documents")

    try:
        loader = DirectoryLoader(
            "knowledge-base",
            glob="**/*.txt",
            loader_cls=TextLoader
        )

        documents = loader.load()

        logger.info(
            "Loaded %s documents from knowledge base",
            len(documents)
        )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(documents)

        logger.info(
            "Created %s document chunks",
            len(chunks)
        )

        return chunks

    except Exception:
        logger.exception("Failed to load knowledge base")
        raise

def add_documents_to_vectorstore():
    """
    Add documents to the vectorstore
    """

    logger.info("Adding documents to vectorstore")

    try:
        vectorstore = create_vectorstore()
        chunks = load_knowledge_base()

        vectorstore.add_documents(
            chunks
        )

        logger.info(
            "Successfully added %s documents to vectorstore",
            len(chunks)
        )

    except Exception:
        logger.exception(
            "Failed to add documents to vectorstore"
        )
        raise

if __name__ == "__main__":
    add_documents_to_vectorstore()