import time
from openai import OpenAI

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
    if thread_id == "":
        empty_thread = client.beta.threads.create()
        thread_id = empty_thread.id
    text = history[-1][0]
    # response = send_message(history)
    response = send_assistants(text, thread_id)
    history[-1][1] = response

    return history, thread_id


def clean():
    return None


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


