import os
from dotenv import load_dotenv
load_dotenv()

import json
from pathlib import Path
from huggingface_hub import CommitScheduler
from uuid import uuid4
from datetime import datetime

HF_DATASET_NAME = os.environ.get('HF_DATASET_NAME')
HF_TOKEN = os.environ.get('HF_TOKEN')

JSON_DATASET_DIR = Path("json_dataset")
JSON_DATASET_DIR.mkdir(parents=True, exist_ok=True)
JSON_DATASET_PATH = JSON_DATASET_DIR / f"{uuid4()}.json"

scheduler = CommitScheduler(
    repo_id=HF_DATASET_NAME,
    repo_type="dataset",
    token=HF_TOKEN,
    folder_path=JSON_DATASET_DIR,
    path_in_repo="data",
    every=1
)

def save_json(input: str, output: str, model_parameters: dict) -> None:
    with scheduler.lock:
        with JSON_DATASET_PATH.open("a") as f:
            json.dump({"input": input, "output": output, "model_parameters": model_parameters, "datetime": datetime.now().isoformat()}, f)
            f.write("\n")