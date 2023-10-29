import gradio as gr
from AinaTheme import AinaGradioTheme
from transformers import pipeline
import gradio as gr
from gradio.components import Textbox, Button, HighlightedText, Markdown

import os
from dotenv import load_dotenv
load_dotenv()

from submit_input import process_input
from utils import check_max_characters

MAX_INPUT_CHARACTERS= int(os.environ.get("MAX_INPUT_CHARACTERS", default=1000))

prompt_examples = ["Prompt example", "Prompt example", "Prompt example"]

def clear():
    return (
        None, 
        None,
    )

with gr.Blocks(**AinaGradioTheme().get_kwargs()) as demo:
    with gr.Row():
        with gr.Column():
           gr.Markdown(
                """# {{cookiecutter.project_name}}
                
                ✨ **[Model explanation]()** .

                🧪 **Intended use**: 

                ⚠️ **Limitations**:

                👀 **Learn more about {{cookiecutter.project_name}}:** .
                
                """
            )
            
    with gr.Row( equal_height=True):
        with gr.Column(variant="panel"):
            placeholder_max_characters = Textbox(
                visible=False,
                interactive=False,
                value= MAX_INPUT_CHARACTERS
            )
            input_ = Textbox(
                lines=3,
                label="Input",
                placeholder="e.g. Enter sentence here"
            )
            with gr.Row(variant="panel", equal_height=True):
                gr.HTML("""<span id="countertext" style="display: flex; justify-content: start; color:#ef4444; font-weight: bold;"></span>""")
                gr.HTML(f"""<span id="counter" style="display: flex; justify-content: end;"> <span id="inputlenght">0</span>&nbsp;/&nbsp;{MAX_INPUT_CHARACTERS}</span>""")


        with gr.Column(variant="panel"):
            output = HighlightedText(
                container=True,
                label="Output",
            )
            with gr.Row(variant="panel"):
                clear_btn = Button(
                    "Clear", 
                )
                submit_btn = Button(
                    "Submit", 
                    variant="primary",
                )
   
    with gr.Row():
        with gr.Column():
            for example in prompt_examples:
                gr.Examples(
                    label="Example",
                    examples=[
                        [example],
                    ],
                    inputs=[input_],
                    outputs=output,
                    fn=process_input,
                )

    input_.change(
        fn=check_max_characters, 
        inputs=[input_, placeholder_max_characters],
        outputs=[clear_btn, submit_btn]
    )

    input_.change(fn=None, inputs=[input_, placeholder_max_characters], _js="""(i, m) => {
        document.getElementById('countertext').textContent =  i.length > m && 'Max length ' + m + ' characters. ' || ''
        document.getElementById('inputlenght').textContent = i.length + '  '
        document.getElementById('inputlenght').style.color =  (i.length > m) ? "#ef4444" : "";
    }""")

    clear_btn.click(
        fn=clear, 
        inputs=[], 
        outputs=[input_, output],
        queue=False
    )
    
    submit_btn.click(
        fn=process_input, 
        inputs=[input_],
        outputs=[output]
    )

if __name__ == "__main__":
    demo.queue(concurrency_count=1, api_open=False)
    demo.launch(show_api=False, server_name='0.0.0.0')