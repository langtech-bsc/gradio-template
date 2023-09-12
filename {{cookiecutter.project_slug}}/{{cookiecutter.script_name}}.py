import gradio as gr
from gradio.components import Textbox, Button, Slider, Checkbox
from AinaTheme import AinaGradioTheme

callback = gr.CSVLogger()

def submit_input(input_, max_new_tokens, repetition_penalty, top_k, top_p, do_sample, num_beams, temperature):
    return (
        input_, 
        gr.update(interactive = True), 
        gr.update(interactive = True)
    )

def change_interactive(text):
    input_state = text
    if input_state.strip() != "":
        return gr.update(interactive = True)
    else:
        return gr.update(interactive = False)

def clean(): 
    return (
        None, 
        None,
        gr.Button.update(interactive=False),
        gr.Button.update(interactive=False),
        gr.Slider.update(value=100),
        gr.Slider.update(value=1.2),
        gr.Slider.update(value=50),
        gr.Slider.update(value=0.95),
        gr.Checkbox.update(value=True),
        gr.Slider.update(value=4),
        gr.Slider.update(value=0.5),
    )
    
def disable_flag_button():
    return  (
        gr.Button.update(interactive=False), 
        gr.Button.update(interactive=False)
    )


with gr.Blocks(**AinaGradioTheme().get_kwargs()) as demo:
    with gr.Row():
        with gr.Column():
            input_ = Textbox(
                lines=10, 
                label="Input"
            )

            max_new_tokens = Slider(
                minimum=1, 
                maximum=200, 
                step=1, 
                value=100,
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
                minimum=0, 
                maximum=100, 
                step=1, 
                value=50, 
                label="Top k"
            )

            top_p = Slider(
                minimum=0, 
                maximum=1, 
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
            
        with gr.Column():
            output = Textbox(
                lines=10, 
                label="Output", 
                interactive=False, 
                show_copy_button=True
            )

            with gr.Row(equal_height=True):
                btnPositive = gr.Button("👍",interactive = False)

                btnNegative= gr.Button("👎", interactive = False)

            with gr.Row():
                clear_btn = Button("Clean", interactive=False)

                submit_btn = Button("Submit",  variant="primary", interactive=False)

    callback.setup([input_, output], "flagged_data_points")

    for button in [submit_btn, clear_btn]:
        input_.change(fn=change_interactive, inputs=[input_], outputs=button)

    for button in [btnPositive, btnNegative]:
        button.click(fn=disable_flag_button, outputs=[btnPositive, btnNegative])

    btnPositive.click(
        lambda *args: callback.flag(args, flag_option="positive"),
        [input_, output], 
        None, 
        preprocess=False
    )
    
    btnNegative.click(
        lambda *args: callback.flag(args, flag_option="negative"),
        [input_, output], 
        None, 
        preprocess=False
    )

    clear_btn.click(
        fn=clean, 
        inputs=[], 
        outputs=[input_, output, btnPositive, btnNegative, max_new_tokens, repetition_penalty, top_k, top_p, do_sample, num_beams, temperature], 
        queue=False
    )

    submit_btn.click(
        fn=submit_input, 
        inputs=[input_, max_new_tokens, repetition_penalty, top_k, top_p, do_sample, num_beams, temperature], 
        outputs=[output, btnPositive, btnNegative]
    )
    
demo.queue(concurrency_count=1, api_open=False)
demo.launch(show_api=False)
