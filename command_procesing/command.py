from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def comparing(sequence_0, sequence_1):
    model_name = "bert-base-cased-finetuned-mrpc"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokens = tokenizer.encode_plus(sequence_0, sequence_1, return_tensors="pt")
    classification_logits = model(**tokens)[0]
    results = torch.softmax(classification_logits, dim=1).tolist()[0]
    return round(results[1] * 100)


# Wheather = "wants to know what's the weather like now", "wants to know what is the wheather for tomorrow", "wants to know what was the whether yesterday or previous days"
# Music = "wants to listen music", "wants to open music player", "open music player"
# Image Description = "wants to know what is the description of the image"
# News = "wants to know what is the latest news" "wants to know news from yesterday"