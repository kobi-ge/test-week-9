from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path


app = FastAPI(title="Items API", version="1.0.0")

class Item(BaseModel):
    name: str
    quantity: str

def create_shopping_list():
    with open("db/shopping_list.json", "w") as f:
        f.write("[]")
create_shopping_list()

DB_PATH = Path("db/shopping_list.json")

def load_database():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        raise ValueError("Database file is not valid JSON.")


@app.get("/items")
def get_items():
    data = load_database()
    return data


def update_db(updated_data):
    with open("db/shopping_list.json", "w") as f:
        json.dump(updated_data, f, indent=2)

def create_dict(item: Item):
    data = {"name": item.name, "quantity": item.quantity}
    return data

@app.post("/item")
def add_item(item: Item):
    data = load_database()
    item = create_dict(item)
    new_id = str(len(data) + 1)
    item[id] = new_id
    data.append(item)
    update_db(data)
    return data


    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)
