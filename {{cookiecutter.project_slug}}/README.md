## install
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

## environment variables
Create an .env file on the root of the project to consume environment variables.

```
MAX_INPUT_CHARACTERS= 2000
SHOW_MODEL_PARAMETERS_IN_UI = "True"
```

## usage
```bash
source venv/bin/activate
python {{cookiecutter.script_name}}.py
```

Open http://127.0.0.1:7860 in your browser (or the url that prints the {{cookiecutter.script_name}}.py program when executed) 

## deactivate
```bash
deactivate
```
