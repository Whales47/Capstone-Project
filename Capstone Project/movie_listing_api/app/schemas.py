from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
