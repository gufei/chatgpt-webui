import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from tools.input import SearchInput


class PdfTool(BaseTool):
    name = "pdf"
    description = "这个工具会向用户发送PDF文档资料，当用户希望获得文档资料、详细资料时，或者咨询是否有文档资料、详细资料时，可以使用pdf这个工具。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')

    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return "已发送PDF资料"
