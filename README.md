# Gradio demo template

Repo templating for Gradio demos using the cookiecutter utility.

| Template Name  | Description                                   |
| -------------  | --------------------------------------------- |
| 1. Standard    | Basic input-output template.                  |
| 2. Sagemaker   | Sagemaker endpoint template.                 |
| 3. Multiner    | Named Entity Recognition (NER) template.     |

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
### 3. Create a project from the template

Create a gradio project using the cookiecutter cli utility

```
cookiecutter https://github.com/langtech-bsc/gradio-template
```
