import gradio as gr

def check_max_characters(text, max_char):
    if len(text.strip()) > int(max_char):
        return gr.update(interactive = True),  gr.update(interactive = False)
    return gr.update(interactive = True),  gr.update(interactive = True)

def clear(): 
    return (
        None, 
        None,
        gr.Slider.update(value=100),
        gr.Slider.update(value=1.2),
        gr.Slider.update(value=50),
        gr.Slider.update(value=0.95),
        gr.Checkbox.update(value=True),
        gr.Slider.update(value=4),
        gr.Slider.update(value=0.5),
    )