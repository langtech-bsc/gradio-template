# Gradio demo template

Repo templating for Gradio demos using the cookiecutter utility.

| Template Name  | Description                                   |
| -------------  | --------------------------------------------- |
| 1. Standard    | Basic input-output template.                  |
| 2. Sagemaker   | Sagemaker endpoint template.                  |
| 3. Multiner    | Named Entity Recognition (NER) template.      |

## Usage

### 1. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install `cookiecutter`
```
pip install cookiecutter
```

### 3. Create a project using the cookiecutter cli
```
cookiecutter https://github.com/langtech-bsc/gradio-template
```

### 4. Start the project from the template

### Start with docker:
```bash
make deploy
```

### Start with PIP: 
```bash
pip install -r requirements.txt
python {{cookiecutter.script_name}}.py
```

### If required create an .env file on the root of the project to consume variables
```
MAX_INPUT_CHARACTERS= 2000
SHOW_MODEL_PARAMETERS_IN_UI = "True"

```
Open http://127.0.0.1:7860 in your browser (or the url that prints the {{cookiecutter.script_name}}.py program when executed) 

## License
This project is distributed under the Apache-2.0 license. See the [LICENSE](https://github.com/langtech-bsc/gradio-template/blob/LICENSE) file for more information.
