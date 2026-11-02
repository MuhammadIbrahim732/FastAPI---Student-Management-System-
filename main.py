from fastapi import FastAPI
from routers.students import router as student_router

app = FastAPI(
    title="Student Management API",
    description="Practice project for learning FastAPI",
    version="1.0.0",
)

app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}
