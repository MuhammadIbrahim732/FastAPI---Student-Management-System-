# 🎓 Student Management API

A RESTful API for managing student records, built with **FastAPI**. Supports full CRUD, filtering, sorting, pagination, and quick statistics. Data is stored in a JSON file, which keeps the project simple while learning FastAPI.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-009688)
![Pydantic](https://img.shields.io/badge/Pydantic-v2-e92063)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- Full CRUD: create, read, replace (PUT), partially update (PATCH), delete
- Filter by department and minimum CGPA
- Sort by CGPA (ascending or descending)
- Pagination with `limit` and `offset`
- Topper and statistics endpoints
- Request validation with Pydantic (including email validation)
- Duplicate email protection (`409 Conflict`)
- Auto-generated IDs (`S001`, `S002`, ...)
- Interactive docs with Swagger UI and ReDoc

---

## 📁 Project Structure

```
.
├── main.py                  # App entry point
├── routers/
│   └── students.py          # Student endpoints
├── schemas/
│   └── student.py           # Pydantic models (Create / Update / Patch)
├── services/
│   └── students.py          # JSON file storage + ID generation
├── data/
│   └── dummy_students.json  # Data store
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi "uvicorn[standard]" "pydantic[email]"
```

> `pydantic[email]` is required for `EmailStr` validation.

### 4. Run the server

```bash
uvicorn main:app --reload
```

The API runs at **http://127.0.0.1:8000**

---

## 📖 API Documentation

| Docs       | URL                         |
| ---------- | --------------------------- |
| Swagger UI | http://127.0.0.1:8000/docs  |
| ReDoc      | http://127.0.0.1:8000/redoc |

---

## 🔌 Endpoints

| Method | Endpoint                | Description                                  |
| ------ | ----------------------- | -------------------------------------------- |
| GET    | `/`                     | Welcome message                              |
| GET    | `/students`             | List students (filter, sort, paginate)       |
| GET    | `/students/{id}`        | Get a student by ID                          |
| GET    | `/students/topper`      | Student with the highest CGPA                |
| GET    | `/students/stats`       | Total students, average CGPA, enrolled count |
| POST   | `/students`             | Create a student (`201`)                     |
| PUT    | `/students/{id}`        | Replace a student completely                 |
| PATCH  | `/students/{id}`        | Update selected fields only                  |
| DELETE | `/students/{id}`        | Delete a student                             |

### Query parameters for `GET /students`

| Parameter      | Type            | Description                                  |
| -------------- | --------------- | -------------------------------------------- |
| `department`   | string          | Filter by department (case-insensitive)      |
| `min_cgpa`     | float (0–4)     | Minimum CGPA                                 |
| `sort_by_cgpa` | `asc` \| `desc` | Sort by CGPA                                 |
| `limit`        | int (1–100)     | Items per page (default `10`)                |
| `offset`       | int (≥ 0)       | Items to skip (default `0`)                  |

**Example:** `GET /students?department=Computer Science&min_cgpa=3.0&sort_by_cgpa=desc&limit=5`

```json
{
  "total": 12,
  "limit": 5,
  "offset": 0,
  "items": [
    {
      "id": "S001",
      "name": "Ali Khan",
      "email": "ali@example.com",
      "age": 21,
      "department": "Computer Science",
      "semester": 5,
      "cgpa": 3.8,
      "is_enrolled": true
    }
  ]
}
```

### Create a student: `POST /students`

```json
{
  "name": "Ali Khan",
  "email": "ali@example.com",
  "age": 21,
  "department": "Computer Science",
  "semester": 5,
  "cgpa": 3.8,
  "is_enrolled": true
}
```

### Statistics: `GET /students/stats`

```json
{
  "total_students": 25,
  "average_cgpa": 3.42,
  "enrolled_students": 22
}
```

---

## ✅ Validation Rules

| Field         | Rule                           |
| ------------- | ------------------------------ |
| `name`        | 2–100 characters               |
| `email`       | Valid email, must be unique    |
| `age`         | 16–100                         |
| `department`  | String                         |
| `semester`    | 1–12                           |
| `cgpa`        | 0.0–4.0                        |
| `is_enrolled` | Boolean (default `true`)       |

### Error responses

| Status | Meaning                                              |
| ------ | ---------------------------------------------------- |
| `404`  | Student not found / no students available            |
| `409`  | Email already exists                                 |
| `422`  | Validation error (e.g. `null` value in a PATCH body) |

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**: web framework
- **Pydantic v2**: data validation
- **Uvicorn**: ASGI server
- **JSON file**: lightweight storage

---

## 🔮 Future Improvements

- Replace JSON storage with a database (SQLite / PostgreSQL + SQLAlchemy)
- Authentication (JWT)
- Search by name
- Unit tests with `pytest`
- Docker support

---

## 👤 Author

**Ibrahim**
BS Software Engineering, National Textile University (NTU), Faisalabad

🔗 [LinkedIn](https://linkedin.com/in/muhammad-ibrahim-python)

---

## 📄 License

This project is licensed under the MIT License.
