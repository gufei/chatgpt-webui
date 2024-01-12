import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from tools.input import SearchInput


class ManualTool(BaseTool):
    name = "manual"
    description = "这个工具帮助用户转人工客服，如果用户要求转接人工客服、用户咨询产品价格、用户进行投诉、用户邀约面谈、或者要求通电话或视频通话，可以使用这个manual工具进行转人工处理。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')

    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return "已转人工处理"
