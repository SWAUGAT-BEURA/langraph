from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class NumbersAPIToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    number: int = Field(..., description="The number to get a fact about.")
    type: str = Field(
        default="trivia",
        description="The type of fact to retrieve. Options are 'trivia', 'math', 'date', or 'year'."
    )
class NumbersAPITool(BaseTool):
    name: str = "numbers_api_tool"
    description: str = (
        "It takes a number and returns a fact about it based on the type of number (e.g., trivia, math, date, or year)."
    )
    args_schema: Type[BaseModel] = NumbersAPIToolInput

    def _run(self, number: int, type: str) -> str:
        # Implementation goes here
        url= f"http://numbersapi.com/{number}/{type}"
        try:
            result = requests.get(url)
            if result.status_code == 200:
                return result.text
            else:
                return f"Error: {result.status_code}"
        except Exception as e:
            return f"Error: {e}"