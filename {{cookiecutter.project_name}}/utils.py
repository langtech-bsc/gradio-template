import gradio as gr

def check_max_characters(text, max_char):
    if len(text.strip()) > int(max_char):
        return gr.update(interactive = True),  gr.update(interactive = False)
    return gr.update(interactive = True),  gr.update(interactive = True)

