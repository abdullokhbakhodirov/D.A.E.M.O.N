from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


def comparing(list_of_sentences, target_sentence):
    model_name = "bert-base-cased-finetuned-mrpc"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    results = []
    for sentence in list_of_sentences:
        tokens = tokenizer.encode_plus(sentence, target_sentence, return_tensors="pt")
        classification_logits = model(**tokens)[0]
        result = torch.softmax(classification_logits, dim=1).tolist()[0]
        results.append(round(result[1] * 100))

    return results


# Wheather = "wants to know what's the weather like now", "wants to know what is the wheather for tomorrow", "wants to know what was the whether yesterday or previous days"
# Music = "wants to listen music", "wants to open music player", "open music player"
# Image Description = "wants to know what is the description of the image"
# News = "wants to know what is the latest news" "wants to know news from yesterday"
