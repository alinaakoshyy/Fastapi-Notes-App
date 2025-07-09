# NOTES API USING FASTAPI AND MONGODB

from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi import status
from fastapi import HTTPException
from pymongo import MongoClient
from dotenv import load_dotenv
from fastapi import Query
import os

app = FastAPI()


class NoteIn(BaseModel):
    priority: Optional[str] = "moderate"  # Default priority is "moderate"
    title: str
    content: str


class Fullnote(BaseModel):
    note_id: int
    created_at: datetime


# In-memory storage for notes (for demonstration purposes)
notes: List[Fullnote] = []  # This will be replaced by MongoDB storage

# Load environment variables from .env file
load_dotenv()
MONGOURI = os.getenv("MONGO_URI")
# Initialize MongoDB client
client = MongoClient(MONGOURI)
db = client["notesdb"]           # Use the database named "notesdb"
notes_collection = db["notes"]   # Use the collection named "notes"

next_note_id = 1  # This will be replaced by MongoDB's ObjectId


@app.post("/add_note", status_code=status.HTTP_201_CREATED)
def add_note(note: NoteIn):  # NoteIn is a Pydantic model for input validation
    note_dict = note.dict()
    note_dict["created_at"] = datetime.now()  # Add created_at timestamp
    # Get the last note to determine the next ID
    last_note = notes_collection.find_one(sort=[("note_id", -1)])
    note_dict["note_id"] = last_note["note_id"] + \
        1 if last_note else 1  # Increment note_id
    notes_collection.insert_one(note_dict)  # Insert the note into MongoDB
    return {"message": "Note added successfully"}


@app.get("/get_notes")
def get_notes(search: Optional[str] = Query(None), note_id: Optional[int] = Query(None)):
    result = []

    # 1. Search by note_id
    if note_id is not None:
        note = notes_collection.find_one({"note_id": note_id})
        if note:
            note["_id"] = str(note["_id"])
            return {"notes": [note]}
        raise HTTPException(status_code=404, detail="Note not found")

    # 2. Search by keyword in title or content (case-insensitive)
    if search:
        filtered = notes_collection.find({
            "$or": [
                {"title": {"$regex": search, "$options": "i"}},
                {"content": {"$regex": search, "$options": "i"}}
            ]
        })
    else:
        # Sort by created_at in descending order
        filtered = notes_collection.find().sort("created_at", -1)

    # 3. Format the output
    for note in filtered:
        note["_id"] = str(note["_id"])
        result.append(note)

    return {"notes": result}


@app.put("/update_note/{note_id}")
def update_note(note_id: int, updated_note: NoteIn):
    updated_data = {
        "title": updated_note.title,
        "content": updated_note.content,
        "priority": updated_note.priority
    }
    result = notes_collection.update_one(
        {"note_id": note_id}, {"$set": updated_data}
    )
    if result.modified_count == 1:
        return {"message": f"Note with ID {note_id} updated successfully"}
    raise HTTPException(
        status_code=404,
        detail=f"Note with ID {note_id} not found"
    )


@app.delete("/delete_note/{note_id}")
def delete_note(note_id: int):
    result = notes_collection.delete_one({"note_id": note_id})
    if result.deleted_count == 1:
        return {"message": f"Note with ID {note_id} deleted successfully"}

    raise HTTPException(
        status_code=404,
        detail=f"Note not found"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
# To run the FastAPI application, use the command:
# uvicorn main:app --reload
