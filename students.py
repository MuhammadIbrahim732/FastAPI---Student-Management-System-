import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).parent.parent
    / "data"
    / "dummy_students.json"
)


def load_students():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_students(students):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def generate_student_id(students):
    numbers = [
        int(s["id"][1:])
        for s in students
        if s["id"].startswith("S") and s["id"][1:].isdigit()
    ]

    return f"S{max(numbers, default=0) + 1:03d}"
