from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict_fake_news
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uuid
import os


""" 
Important thing to add:
In production, you should tighten allow_origins:
allow_origins=["https://your-frontend-domain.com"]
only allow my frontend to call this backend
"""

app = FastAPI(title="Fake News Detector API", version="1.0.0")

# Get allowed origins from environment variable or use default
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/result", StaticFiles(directory="result"), name="result")

class StatementInput(BaseModel):
    statement: str

@app.get("/")
def read_root():
    return {"message": "Fake News Detector API is running!", "status": "healthy"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is operational"}

@app.post("/analyze")
def analyze(input: StatementInput):
    return predict_fake_news(input.statement, save_plot_path=f"static/shap_waterfall_{uuid.uuid4().hex}.png")


