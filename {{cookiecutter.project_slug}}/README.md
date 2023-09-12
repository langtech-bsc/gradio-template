## install
```bash
python3 -m venv env
source env/bin/activate
pip install wheel && pip install -r requirements.txt
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
