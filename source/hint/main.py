# Import Union since oir Item object will have tags that can be strings or a list.
from socketserver import ThreadingUnixDatagramServer
from typing import Union

from fastapi import FastAPI

# BaseModel from pydantic is used to define data objects
from pydantic import BaseModel

# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

app = FastAPI()

# This allows sending of data (our TaggedItem) via POST to the API
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item