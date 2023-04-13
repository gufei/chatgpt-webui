import openai

openai.debug = True
openai.log = 'debug'


def add_text(history, text):
    history = history + [(text, None)]
    return history, ""


def bot(history):
    response = send_message(history)
    history[-1][1] = response

    return history


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
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.75,
            messages=message
        )
        return res.choices[0].message.content
    except Exception as e:
        return str(e)
