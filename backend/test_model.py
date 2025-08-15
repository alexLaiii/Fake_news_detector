import torch
from transformers import AutoTokenizer, AutoModel
from model.model_arch import BERT_Arch
import numpy as np

# Load model
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
bert = AutoModel.from_pretrained('bert-base-uncased')
model = BERT_Arch(bert)
model.load_state_dict(torch.load('model/fake_news_model.pt', map_location='cpu'))
model.eval()

def test_news(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        output = model(inputs["input_ids"], inputs["attention_mask"])
        probs = torch.exp(output)
        pred = torch.argmax(probs, dim=1).item()
        conf = probs[0][pred].item()
    return "FAKE" if pred == 1 else "REAL", round(conf, 4)

# Test cases
test_cases = [
    # Real news examples
    ("NASA's James Webb Space Telescope discovers distant galaxy", "REAL"),
    ("COVID-19 vaccine approved by FDA", "REAL"),
    ("Tesla reports record quarterly earnings", "REAL"),
    ("Scientists discover new species in Amazon rainforest", "REAL"),
    
    # Obviously fake news
    ("Aliens contact Earth through social media", "FAKE"),
    ("Scientists create time machine using household items", "FAKE"),
    ("Government admits to hiding dragons in mountains", "FAKE"),
    ("New study shows chocolate cures all diseases", "FAKE"),
    
    # Ambiguous/clickbait
    ("Shocking discovery will change everything you know", "UNCLEAR"),
    ("You won't believe what happened next", "UNCLEAR"),
    ("This one weird trick doctors don't want you to know", "UNCLEAR"),
]

print("🧪 Testing Fake News Detector Model")
print("=" * 50)

correct = 0
total = 0

for text, expected in test_cases:
    prediction, confidence = test_news(text)
    
    # Score only clear cases
    if expected in ["REAL", "FAKE"]:
        if prediction == expected:
            correct += 1
            result = "✅ CORRECT"
        else:
            result = "❌ WRONG"
        total += 1
    else:
        result = "🤔 AMBIGUOUS"
    
    print(f"\n📰 Text: {text}")
    print(f"🎯 Expected: {expected}")
    print(f"🤖 Predicted: {prediction} (confidence: {confidence})")
    print(f"📊 Result: {result}")

if total > 0:
    accuracy = (correct / total) * 100
    print(f"\n📈 Overall Accuracy: {accuracy:.1f}% ({correct}/{total})")
    
    if accuracy >= 80:
        print("🎉 EXCELLENT - Your model is performing very well!")
    elif accuracy >= 70:
        print("👍 GOOD - Your model is performing well")
    elif accuracy >= 60:
        print("⚠️ FAIR - Room for improvement")
    else:
        print("❌ NEEDS WORK - Model needs more training/data")
else:
    print("\n⚠️ No clear test cases to evaluate accuracy") 