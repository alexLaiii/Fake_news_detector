# Fake News Detector (Work In Progress)

A work-in-progress full-stack project for detecting fake news using a fine-tuned BERT model with SHAP visualizations.

# Project Structure
fake_news_detector/

├── frontend/ # Next.js + Tailwind frontend UI
├── backend/ # Python backend with BERT model + SHAP

# Tools
- **Frontend**: Next.js, Tailwind CSS, React, ShadCN UI
- **Backend**: PyTorch, Hugging Face Transformers, SHAP, FastAPI 
- **Model**: BERT fine-tuned, base model:(bert-based-uncased)

# Status

> This project is under active development.  
Not yet production-ready — some components may break or be incomplete.

##  Setup Instructions (WIP)

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn app:app --reload

# Frontend (Make sure you have Node.js and Next.js installed)
cd frontend
npm install
npm run dev
