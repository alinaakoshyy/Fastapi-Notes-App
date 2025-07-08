# NOTES API

from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


class NoteIn(BaseModel):
    priority: str
    title: str
    content: str


class Fullnote(BaseModel):
    note_id: int
    priority: str
    title: str
    content: str
    created_at: datetime


notes: List[Fullnote] = []
next_note_id = 1


@app.post("/add_note")
def add_note(note: NoteIn):  # NoteIn is a Pydantic model for input validation
    global next_note_id
    new_note = Fullnote(
        note_id=next_note_id,
        priority=note.priority,
        title=note.title,
        content=note.content,
        created_at=datetime.now()
    )
    next_note_id += 1
    notes.append(new_note)
    return {"message": "Note added successfully"}


@app.get("/get_notes")
def get_notes(search: Optional[str] = None):
    if search:    # If a search query is provided, filter the notes 
        search_lower = search.lower()  # Convert search term to lowercase for case-insensitive comparison     
        filtered_notes = [
            note for note in notes 
            if search_lower in note.title.lower() or search_lower in note.content.lower()] # case-insensitive search
        return {"notes": filtered_notes}
    return {"notes": notes}    # If no search query, return all notes


@app.put("/update_note/{note_id}")
def update_note(note_id: int, updated_note: NoteIn):
    for note in notes:
        if note.note_id == note_id:
            note.title = updated_note.title
            note.content = updated_note.content
            return {"message": f"Note with ID {note_id} updated successfully"}
    return {"error": "Note not found"}


@app.delete("/delete_note/{note_id}")
def delete_note(note_id: int):
    for note in notes:
        if note.note_id == note_id:
            notes.remove(note)
            return {"message": f"Note with ID {note_id} deleted successfully"}
    # If the note ID is not found, return an error message
    return {"error": "Note ID out of range"}
