from pydantic import BaseModel

class TestMarks(BaseModel):
    test1: int 
    test2: int 
    internal: int 