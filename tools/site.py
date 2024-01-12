import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from tools.input import SearchInput


class SiteTool(BaseTool):
    name = "site"
    description = "这个工具会向用户发送官网链接，当用户希望自行查看系统，或者用户咨询官网地址时，可以使用site这个工具。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')
    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return "已发送官网链接"
