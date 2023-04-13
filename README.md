# ChatGPT WebUI

Python version >= 3.10

need to set the `OPENAI_API_KEY` environment variables. 

If you are using cf worker, please also set the `OPENAI_API_BASE` environment variables. 

Run this from the project root directory.

```bash
export OPENAI_API_KEY=your_openai_api_key

pip install -r requirements.txt

gradio main.py
```

This project UI was created using [gradio](https://gradio.app/)


