from transformers import RobertaForSequenceClassification, RobertaTokenizer
import pandas as pd
import torch

# Load your text data
data = pd.read_csv('cleaned_comments1.csv')
print(data.head())
# Load a pre-trained RoBERTa model and tokenizer
model_name = "roberta-base"
tokenizer = RobertaTokenizer.from_pretrained(model_name)
model = RobertaForSequenceClassification.from_pretrained(model_name, num_labels=4)  # Adjust the number of labels

# Tokenize the text data
encodings = tokenizer(list(data['0']), truncation=True, padding=True, return_tensors="pt")

# Prepare labels (assuming you have one-hot encoded labels in your dataset)
labels = torch.tensor(data[['positive', 'angry', 'confused', 'hate_speech']].values)

# Fine-tune the model
# ... (code for model fine-tuning)

# Inference
with torch.no_grad():
    inputs = {key: value.to(model.device) for key, value in encodings.items()}
    outputs = model(**inputs)
    logits = outputs.logits

# Extract predicted sentiment labels
predicted_labels = torch.argmax(logits, dim=1).tolist()

print(predicted_labels)