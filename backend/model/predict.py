import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
from model.model_arch import BERT_Arch
import shap
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
bert = AutoModel.from_pretrained('bert-base-uncased')
model = BERT_Arch(bert)
model.load_state_dict(torch.load('model/fake_news_model.pt', map_location='cpu'))
model.eval()

# Predict class + confidence
def get_prediction(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = model(inputs["input_ids"], inputs["attention_mask"])
        probs = torch.exp(output)
        pred = torch.argmax(probs, dim=1).item()
        conf = probs[0][pred].item()
    return pred, conf



def predict_prob(texts):
    texts = list(map(str, texts))
    tokens = tokenizer(
        texts,
        return_tensors="pt",
        padding=True,
        truncation=True
    )
    input_ids = tokens["input_ids"]
    attention_mask = tokens["attention_mask"]

    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        probs = torch.exp(outputs)  # Convert from log-softmax to normal probs

    return probs.numpy()

# main prediction function
def predict_fake_news(statement, save_plot_path = None):
    # Step 1: Get predicted label and confidence
    pred_label, base_conf = get_prediction(statement)

    # Step 2: Run SHAP explainer
    shap_values = explainer([statement])
    sv = shap_values[0]  # Only one input, so just take the first result

    # Step 3: Extract SHAP values for the predicted class only
    token_impacts = []
    for token, value in zip(sv.data, sv.values):
        # sv.values is (num_tokens, num_classes)
        if isinstance(value, (list, np.ndarray)):
            impact = float(value[pred_label])  # ← use only the predicted class
        else:
            impact = float(value)
        token_impacts.append((token, impact))

    # Step 4: Sort tokens by absolute impact value (most influential first)
    token_impacts.sort(key=lambda x: abs(x[1]), reverse=True)

    # Step 5: Select top 5 impactful tokens as "highlights"
    highlights = [token for token, impact in token_impacts[:5]]

    if save_plot_path:
        plt.clf()  # Clear previous figure
        # Keep only SHAP values for the predicted class
        sv.values = sv.values[:, pred_label]
        sv.base_values = sv.base_values[pred_label]
        shap.plots.waterfall(sv, show=False)
        plt.tight_layout()
        plt.savefig(save_plot_path)
        plt.close()

    return {
        "label": "fake" if pred_label == 1 else "real",
        "confidence": round(base_conf, 4),
        "highlights": highlights,
        "plot_path": save_plot_path if save_plot_path else None
    }



explainer = shap.Explainer(predict_prob, tokenizer)



