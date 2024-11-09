from pydantic import BaseModel
from pydantic import Field


class InputFile(BaseModel):
    file_content: str = Field(description="File content")
    file_name: str = Field(description="File name")
