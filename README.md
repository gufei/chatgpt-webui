# ChatGPT WebUI

Python version >= 3.10

need to set the `OPENAI_API_KEY` constant. 

If you are using cf worker, please also set the `OPENAI_API_BASE` constant. 

Run this from the project root directory.

```bash
export OPENAI_API_KEY=your_openai_api_key

pip install -r requirement.txt

gradio main.py
```