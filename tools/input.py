from langchain.pydantic_v1 import BaseModel, Field


class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")
