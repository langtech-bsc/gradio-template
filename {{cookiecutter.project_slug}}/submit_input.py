import gradio as gr

# If you want to save data points uncomment the following script.
# The environment variable in save_to_dataset script are required

# from save_to_dataset_hf import save_json


def submit_input(input_, max_new_tokens, repetition_penalty, top_k, top_p, do_sample, num_beams, temperature):
    if input_.strip() == "":  
        gr.Warning('Not possible to inference an empty input')
        return None
    
    model_parameters = {
        "max_new_tokens": max_new_tokens,
        "repetition_penalty": repetition_penalty,
        "top_k": top_k,
        "top_p": top_p,
        "do_sample": do_sample,
        "num_beams": num_beams,
        "temperature": temperature
    }
     
    # e.g output = invoke_endpoint(input_, model_parameters=model_parameters)
    model_output = None

    if model_output is not None:
        print(model_output) 
        # save_json(input_, model_output, model_parameters)
    else:
        gr.Warning('Inference endpoint is not available right now. Please try again later.')
    return model_output