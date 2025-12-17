from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import json
from pathlib import Path


app = FastAPI(title="Items API", version="1.0.0")

DB_PATH = Path("server1/db/shopping_list.json")

def create_shopping_list():
    with open("server1/db/shopping_list.json", "w") as f:
        f.write("[]")

def load_database() -> Dict:
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


@app.get("/items")
def get_items():
    data = load_database()
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)