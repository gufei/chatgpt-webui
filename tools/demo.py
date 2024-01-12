import os

from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from tools.input import SearchInput


class DemoTool(BaseTool):
    name = "demo"
    description = "这个工具会向用户发送客户案例，当用户希望获得客户案例、成功安例时，可以使用demo这个工具。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')

    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return "已发送公众号文章"
