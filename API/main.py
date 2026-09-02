from fastapi import FastAPI
from API.schemas import TestMarks

app = FastAPI()

def calculate(mark: TestMarks):
    test_1 = mark.test1 * 0.2
    test_2 = mark.test2 * 0.3
    test_3 = mark.internal * 0.5
    total = test_1 + test_2 + test_3
    results = total
    return  results

@app.post("/result")
def results(marks: TestMarks):
    final = calculate(marks)
    if final >= 40:
        return {"Semester Mark": final,
                "Message": "You qualify for Final Examination"}
    else:
        return {"Semester Mark": final,
                "Message": "You dont qualify for Final Examination"}

