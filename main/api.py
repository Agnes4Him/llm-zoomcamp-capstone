from datetime import datetime
import logging

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from pydantic import BaseModel, Field, field_validator

from sqlalchemy import text

from app.agent import agent
from app.calculate_cost import calculate_cost
from app.database import engine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: List[Dict] = Field(default_factory=list)

    @field_validator("message")
    @classmethod
    def validate_message(cls, value):

        value = value.strip()

        if not value:
            raise ValueError("Message cannot be empty")

        return value

class FeedbackRequest(BaseModel):
    question: str
    response: str
    rating: str

@app.on_event("startup")
def startup_event():
    logger.info("HealthSecure AI API started successfully")

@app.get("/api/healthcheck")
def health():
    logger.debug("Healthcheck endpoint called")

    return {
        "status": "ok"
    }

@app.post("/api/question")
def chat(request: QuestionRequest):
    logger.info(
        "Received question request. History length: %s",
        len(request.history)
    )

    try:

        messages = []

        for item in request.history:
            messages.append(
                (
                    item["role"],
                    item["content"]
                )
            )

        messages.append(
            (
                "user",
                request.message
            )
        )

        logger.info(
            "Starting agent execution"
        )

        health_agent = agent()

        response = health_agent.invoke(
            {
                "messages": messages
            }
        )

        logger.info(
            "Agent execution completed successfully"
        )

        input_tokens = response["messages"][-1].usage_metadata.get(
            "input_tokens",
            0
        )

        output_tokens = response["messages"][-1].usage_metadata.get(
            "output_tokens",
            0
        )

        cost = calculate_cost(
            input_tokens,
            output_tokens
        )

        logger.info(
            "Request completed. Input tokens: %s, Output tokens: %s, Cost: %.6f",
            input_tokens,
            output_tokens,
            cost
        )

        return {
            "response": response["messages"][-1].content,
            "cost": cost
        }

    except Exception:
        logger.exception(
            "Error occurred while processing question request"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process request at this time"
        )

@app.post("/api/feedback")
def save_feedback(feedback: FeedbackRequest):
    logger.info(
        "Received feedback submission. Rating: %s",
        feedback.rating
    )

    sql = """
    INSERT INTO feedbacks
    (
        question,
        response,
        rating
    )
    VALUES
    (
        :question,
        :response,
        :rating
    )
    """

    try:

        with engine.begin() as conn:

            conn.execute(
                text(sql),
                {
                    "question": feedback.question,
                    "response": feedback.response,
                    "rating": feedback.rating
                }
            )

        logger.info(
            "Feedback saved successfully"
        )


        return {
            "message": "Feedback saved successfully"
        }

    except Exception:
        logger.exception(
            "Failed to save feedback"
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to save feedback"
        )