from pydantic import BaseModel, Field
from typing import Optional

class TransItem(BaseModel):
    content: str
    language: str
    engine: str = "text-davinci-002"
    temperature: float = 1
    max_tokens: int = 1000
    frequency_penalty: float = 0
    presence_penalty: float = 0
