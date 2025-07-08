# 📝 FastAPI Notes App

A simple and clean RESTful API built using **FastAPI**.  
This project allows users to **create**, **view**, **search**, and **delete notes** using API endpoints.

---

## 🚀 Features

- ✅ Add new notes
- ✅ View all notes
- ✅ Search notes by keyword (query param)
- ✅ Delete notes by ID
- ✅ Automatically assigns ID & timestamp to each note

---

## 📦 Tech Stack

- **Python 3**
- **FastAPI**
- **Pydantic**
- **Uvicorn** (for running the server)

---

## ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/alinaakoshyy/Fastapi-Notes-App.git
   cd Fastapi-Notes-App


2. Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt

4. Run the app:
bash
Copy
Edit
uvicorn fastapi2:app --reload

5. Visit Swagger UI at:
arduino
Copy
Edit
http://127.0.0.1:8000/docs

💡 Example Endpoints
Method	Endpoint	Description
POST	/add_note	Add a new note
GET	/get_notes	View all notes
GET	/get_notes?search=milk	Search notes
DELETE	/delete_note/{id}	Delete a note by ID


💚 Made with FastAPI & love by alina