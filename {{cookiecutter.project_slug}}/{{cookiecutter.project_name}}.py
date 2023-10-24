import gradio as gr
from gradio.components import Textbox, Button, Slider, Checkbox
from AinaTheme import AinaGradioTheme

import os
from dotenv import load_dotenv
load_dotenv()

from submit_input import process_input
from utils import check_max_characters, clear

MAX_NEW_TOKENS = int(os.environ.get("MAX_NEW_TOKENS", default=100))
MAX_INPUT_CHARACTERS= int(os.environ.get("MAX_INPUT_CHARACTERS", default=100))
SHOW_MODEL_PARAMETERS_IN_UI = os.environ.get("SHOW_MODEL_PARAMETERS_IN_UI", default=True) == "True"

with gr.Blocks(**AinaGradioTheme().get_kwargs()) as demo:
    with gr.Row():
        with gr.Column(scale=0):
            gr.Image(
                "./assets/BSC-blue.svg",
                elem_id="banner",
                show_label=False,
                show_download_button=False, 
                show_share_button=False
            )
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
                lines=11,
                label="Input",
                placeholder="e.g. El mercat del barri és fantàstic hi pots trobar."
            )
            with gr.Row(variant="panel", equal_height=True):
                gr.HTML("""<span id="countertext" style="display: flex; justify-content: start; color:#ef4444; font-weight: bold;"></span>""")
                gr.HTML(f"""<span id="counter" style="display: flex; justify-content: end;"> <span id="inputlenght">0</span>&nbsp;/&nbsp;{MAX_INPUT_CHARACTERS}</span>""")

            with gr.Row(variant="panel"):
                with gr.Accordion("Model parameters", open=False, visible=SHOW_MODEL_PARAMETERS_IN_UI):
                    max_new_tokens = Slider(
                        minimum=1,
                        maximum=200,
                        step=1,
                        value=MAX_NEW_TOKENS,
                        label="Max tokens"
                    )
                    repetition_penalty = Slider(
                        minimum=0.1,
                        maximum=10,
                        step=0.1,
                        value=1.2,
                        label="Repetition penalty"
                    )
                    top_k = Slider(
                        minimum=1,
                        maximum=100,
                        step=1,
                        value=50,
                        label="Top k"
                    )
                    top_p = Slider(
                        minimum=0.01,
                        maximum=0.99,
                        value=0.95,
                        label="Top p"
                    )  
                    do_sample = Checkbox(
                        value=True, 
                        label="Do sample"
                    )
                    num_beams = Slider(
                        minimum=1, 
                        maximum=8, 
                        step=1,
                        value=4,
                        label="Beams"
                    )
                    temperature = Slider(
                        minimum=0, 
                        maximum=1,
                        value=0.5,
                        label="Temperature"
                    )

                    parameters_compontents = [max_new_tokens, repetition_penalty, top_k, top_p, do_sample, num_beams, temperature]

        with gr.Column(variant="panel"):
            output = Textbox(
                lines=11,
                label="Output",
                interactive=False,
                show_copy_button=True
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
            gr.Examples(
                label="Short prompts:",
                examples=[
                    ["""Prompt example"""],
                ],
                inputs=[input_] + parameters_compontents,
                outputs=output,
                fn=process_input,
            )

            gr.Examples(
                label="Zero-shot prompts",
                examples=[
                    ["Prompt example"],
                ],
                inputs=[input_] + parameters_compontents,
                outputs=output,
                fn=process_input,
            )
            gr.Examples(
                label="Few-Shot prompts:",
                examples=[
                    ["""Prompt example"""],
                ],
                inputs=[input_] + parameters_compontents,
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
        outputs=[input_, output] + parameters_compontents, 
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