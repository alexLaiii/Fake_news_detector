from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_fake_news
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uuid



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")

class StatementInput(BaseModel):
    statement: str

@app.post("/analyze")
def analyze(input: StatementInput):
    return predict_fake_news(input.statement, save_plot_path=f"static/shap_waterfall_{uuid.uuid4().hex}.png")


