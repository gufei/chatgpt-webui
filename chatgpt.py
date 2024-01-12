import time
from openai import OpenAI
from langchain.agents.openai_assistant import OpenAIAssistantRunnable
from langchain.agents import AgentExecutor
from langchain_core.agents import AgentFinish
from tools.video import VideoTool
from tools.demo import DemoTool
from tools.manual import ManualTool
from tools.pdf import PdfTool
from tools.program import ProgramTool
from tools.site import SiteTool

# openai.debug = True
# openai.log = 'debug'

client = OpenAI()


def add_text(history, text):
    # global threadId
    # if len(history) == 0:
    #     empty_thread = OpenAI().beta.threads.create()
    #     threadId = empty_thread.id
    # print(threadId)
    history = history + [(text, None)]
    return history, ""


def bot(history, thread_id):
    # if thread_id == "":
    #     empty_thread = client.beta.threads.create()
    #     thread_id = empty_thread.id
    text = history[-1][0]
    # response = send_message(history)
    # response = send_assistants(text, thread_id)
    # history[-1][1] = response
    response = send_assistants_by_langchain(text, thread_id)
    thread_id = response["thread_id"]
    history[-1][1] = response["output"]

    return history, thread_id


def clean():
    return None





def execute_agent(agent, tools, input):
    tool_map = {tool.name: tool for tool in tools}
    response = agent.invoke(input)
    tool_outputs = []
    while not isinstance(response, AgentFinish):
        tool_outputs = []
        for action in response:
            tool_output = tool_map[action.tool].invoke(action.tool_input)
            print(action.tool, action.tool_input, tool_output, end="\n\n")
            tool_outputs.append(
                {"output": tool_output, "tool_call_id": action.tool_call_id}
            )
        response = agent.invoke(
            {
                "tool_outputs": tool_outputs,
                "run_id": action.run_id,
                "thread_id": action.thread_id,
            }
        )

    if len(tool_outputs) > 0:
        tool_output = tool_outputs[0]["output"]
        return AgentFinish(return_values={
            "output": tool_output,
            "run_id": action.run_id,
            "thread_id": action.thread_id,
        }, log=response.return_values["output"])

    return response


def send_assistants_by_langchain(text, thread_id):
    tools = [
        VideoTool(),
        DemoTool(),
        ManualTool(), PdfTool(), ProgramTool(), SiteTool()
    ]
    agent = OpenAIAssistantRunnable(assistant_id="asst_O3Bi4rWhjQSr9H1sCAwSy2z6", tools=tools, as_agent=True)

    if thread_id == "":
        response = execute_agent(agent, tools, {"content": text})
    else:
        response = execute_agent(agent, tools, {"content": text, "thread_id": thread_id})

    print(response)
    return response.return_values

    # agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # if thread_id == "":
    #     response = agent_executor.invoke({"content": text})
    # else:
    #     response = agent_executor.invoke({"content": text, "thread_id": thread_id})
    # print(response.keys())
    #
    # while True:
    #     retrieve = client.beta.threads.runs.retrieve(
    #         thread_id=thread_id,
    #         run_id=response["run_id"]
    #     )
    #     if retrieve.status not in ["queued", "in_progress"]:
    #         break
    #     time.sleep(1)
    # print(response)
    # return response


def send_message(history):
    message = []
    system = {"role": "system", "content": "You are a helpful assistant."}
    message.append(system)
    for i, content in enumerate(history):
        user = {"role": "user", "content": content[0]}
        message.append(user)
        if content[1]:
            assistant = {"role": "assistant", "content": content[1]}
            message.append(assistant)
    try:
        res = OpenAI().chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.75,
            messages=message
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)


def send_assistants(text, thread_id):
    message = client.beta.threads.messages.create(
        thread_id=thread_id,
        role="user",
        content=text,
    )
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id="asst_O3Bi4rWhjQSr9H1sCAwSy2z6",
    )

    while True:
        retrieve = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
        if retrieve.status not in ["queued", "in_progress"]:
            break
        time.sleep(1)

    if retrieve.status == "completed":
        messages = client.beta.threads.messages.list(
            thread_id=thread_id
        )
        # print(messages.data[0].content[0].text.value)
        return messages.data[0].content[0].text.value
    else:
        return "不好意思，我没能理解您的意思~~"
