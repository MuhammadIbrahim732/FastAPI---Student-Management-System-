from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=16, le=100)
    department: str
    semester: int = Field(ge=1, le=12)
    cgpa: float = Field(ge=0, le=4)
    is_enrolled: bool = True


class StudentUpdate(StudentCreate):
    is_enrolled: bool


class StudentPatch(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(default=None, ge=16, le=100)
    department: Optional[str] = None
    semester: Optional[int] = Field(default=None, ge=1, le=12)
    cgpa: Optional[float] = Field(default=None, ge=0, le=4)
    is_enrolled: Optional[bool] = None
