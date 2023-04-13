import gradio as gr
import chatgpt


def add_file(history, file):
    history = history + [((file.name,), None)]
    return history


with gr.Blocks() as ChatAPP:
    chatbot = gr.Chatbot([], elem_id="chatbot").style(height=750)

    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(
                show_label=False,
                placeholder="prompt......",
            ).style(container=False)
        # with gr.Column(scale=0.15, min_width=0):
        #     btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
        with gr.Column(scale=0.15, min_width=0):
            submit_btn = gr.Button("Chat")

    clean_btn = gr.Button("Clean")

    submit_btn.click(chatgpt.add_text, [chatbot, txt], [chatbot, txt]).then(
        chatgpt.bot, chatbot, chatbot
    )
    txt.submit(chatgpt.add_text, [chatbot, txt], [chatbot, txt]).then(
        chatgpt.bot, chatbot, chatbot
    )
    # btn.upload(add_file, [chatbot, btn], [chatbot]).then(
    #     bot, chatbot, chatbot
    # )
    clean_btn.click(fn=chatgpt.clean, outputs=chatbot)

ChatAPP.launch()

# App = gr.TabbedInterface([ChatAPP], ["ChatGPT"])
# ChatAPP.launch(auth=("admin", "admin"))
