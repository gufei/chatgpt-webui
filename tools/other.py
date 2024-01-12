import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from tools.input import SearchInput


class OtherInput(BaseModel):
    query: str = Field(description="should be a search query")
    thread_id: str


class OtherTool(BaseTool):
    name = "other"
    description = "这是一个兜底的工具，当其他所有的工具都没有命中的时候，进入这个工具进行处理。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')
    args_schema: Type[BaseModel] = OtherInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        print(self.thread_id)
        return "兜底"
