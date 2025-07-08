# 📝 FastAPI Notes App

A simple and lightweight Notes API built using **FastAPI**.  
This project allows you to create, read, update, delete, and search notes — fully functional and tested using Postman.

---

## 🚀 Features

- ✅ Add new notes
- 🔍 Get all notes or search by keyword
- 📄 Get a single note by its ID
- ✏️ Update a note by ID
- ❌ Delete a note by ID
- 🧪 Fully tested with Swagger UI and Postman

---

## 📦 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.11+

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

5. Open your browser:
Swagger UI: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

💡 Example Endpoints
Method	Endpoint	Description
POST	/add_note	Add a new note
GET	/get_notes	View all notes
GET	/get_notes?search=milk	Search notes
DELETE	/delete_note/{id}	Delete a note by ID

🧪 Postman Tips
Body type for POST/PUT: raw → JSON

Example:

json
Copy
Edit
{
  "title": "Dev's Birthday",
  "content": "10th August"
}

💚 Made with FastAPI & love by alina