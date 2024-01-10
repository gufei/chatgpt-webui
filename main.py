import gradio as gr
import chatgpt

userList = {
    'gk': 'gxl'
}


def auth_fn(username="", password=""):
    return userList.get(username) == password


def add_file(history, file):
    history = history + [((file.name,), None)]
    return history


with gr.Blocks() as ChatAPP:
    chatbot = gr.Chatbot([], elem_id="chatbot", height=750)

    thread_id = gr.State("")

    with gr.Row():
        with gr.Column(scale=85):
            txt = gr.Textbox(
                show_label=False,
                placeholder="prompt......",
            )
        # with gr.Column(scale=0.15, min_width=0):
        #     btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
        with gr.Column(scale=15, min_width=0):
            submit_btn = gr.Button("发送")

    clean_btn = gr.Button("清理历史记录")

    submit_btn.click(chatgpt.add_text, [chatbot, txt], [chatbot, txt]).then(
        chatgpt.bot, [chatbot, thread_id], [chatbot, thread_id]
    )
    txt.submit(chatgpt.add_text, [chatbot, txt], [chatbot, txt]).then(
        chatgpt.bot, [chatbot, thread_id], [chatbot, thread_id]
    )
    # btn.upload(add_file, [chatbot, btn], [chatbot]).then(
    #     bot, chatbot, chatbot
    # )
    clean_btn.click(fn=chatgpt.clean, outputs=chatbot)

ChatAPP.launch(auth=auth_fn, server_name='0.0.0.0')
