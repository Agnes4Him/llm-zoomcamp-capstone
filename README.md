## Project structure

healthsecure-ai/

├── app/
│   ├── agent.py          # LangChain agent
│   ├── tools.py          # All tool definitions
│   ├── rag.py            # Pinecone retriever
│   ├── database.py       # PostgreSQL connection
│   ├── prompts.py        # System prompt
│   └── llm.py            # Bedrock LLM configuration
│
├── knowledge_base/
│   ├── 01_member_handbook.md
│   ├── 02_benefits_guide.md
│   ├── 03_coverage_policies.md
│   ├── 04_prior_authorization.md
│   ├── 05_claims_guide.md
│   └── 06_appeals_guide.md
│
├── scripts/
│   ├── ingest_documents.py
│   ├── generate_documents.py
│   └── generate_data.py
│
├── database/
│   └── schema.sql
│
├── .env
├── requirements.txt
└── main.py

## start fastapi app
uv run uvicorn api:app --host 0.0.0.0 --port 5000 --reload
