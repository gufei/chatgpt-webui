import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool
from typing import Optional, Type
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from tools.input import SearchInput


class VideoTool(BaseTool):
    name = "video"
    description = "这个工具会向用户发送演示视频，当用户希望获得演示视频的时候，或者咨询是否有演示视频的时候，可以使用video这个工具。"
    return_direct = True
    verbose = bool(os.getenv("DEBUG") == 'True')

    args_schema: Type[BaseModel] = SearchInput

    def _run(self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None) -> str:
        return "已发送演示视频"
