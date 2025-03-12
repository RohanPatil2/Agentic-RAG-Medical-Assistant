from pydantic import BaseModel, Field
from typing import List, Literal
from typing_extensions import TypedDict


class AgentState(TypedDict):
    """
    Maintains the overall state for an agent, including:
    - The user question
    - A list of document relevance grades
    - The final LLM output
    - Retrieved documents
    - Whether the question is on-topic
    """
    question: str
    grades: List[Literal["Yes", "No"]]
    llm_output: str
    documents: List[str]
    on_topic: bool


class GradeQuestion(BaseModel):
    """
    Determines if a user question is related to a medical context,
    such as medical terminology, diagnosis, or symptoms.
    """
    score: Literal["Yes", "No"] = Field(
        description=(
            "Is the question about medical topics (e.g., medical terms, "
            "diagnosis, symptoms)? If yes -> 'Yes', otherwise -> 'No'."
        )
    )


class GradeDocuments(BaseModel):
    """
    Indicates whether a retrieved document is relevant to the user's question.
    """
    score: Literal["Yes", "No"] = Field(
        description="Documents are relevant to the question: 'Yes' or 'No'."
    )
