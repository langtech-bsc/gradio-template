import gradio as gr

# If you want to save data points uncomment the following script.
# The environment variable in save_to_dataset script are required

# from save_to_dataset_hf import save_json


def compute_output(input):
    #Change this code with yours ...
    return f"This is a sample output for {input}"

def process_input(input):
    if input.strip() == "":  
        gr.Warning('Not possible to process an empty input.')
        return None
    output = compute_output(input=input)

    if output is not None:
        print(output) 
        # save_json(input, output, parameters)
    else:
        gr.Warning('An error ocurred. Please try again later.')
    return output