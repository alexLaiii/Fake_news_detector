from fastapi import FastAPI
from pydantic import BaseModel
from model.predict import predict_fake_news

app = FastAPI()

class StatementInput(BaseModel):
    statement: str

@app.post("/analyze")
def analyze(input: StatementInput):
    return predict_fake_news(input.statement)
