import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModel
from model.model_arch import BERT_Arch

# Load tokenizer and BERT base
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
bert = AutoModel.from_pretrained('bert-base-uncased')

# Rebuild architecture and load weights
model = BERT_Arch(bert)
model.load_state_dict(torch.load('model/fake_news_model.pt', map_location='cpu'))
model.eval()

def predict_fake_news(statement):
    inputs = tokenizer(statement, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = model(inputs["input_ids"], inputs["attention_mask"])
        probs = torch.exp(output)
        pred = torch.argmax(probs, dim=1).item()
        confidence = probs[0][pred].item()
    return {
        "label": "fake" if pred == 1 else "real",
        "confidence": round(confidence, 4)
    }
