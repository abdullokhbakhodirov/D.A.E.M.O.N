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


# ===================================================================================================================================


# Wheather = "wants to know what's the weather like now", "wants to know what is the wheather for tomorrow", "wants to know what was the whether yesterday or previous days"
# Music = "wants to listen music", "wants to open music player", "open music player"
# Image Description = "wants to know what is the description of the image"
# News = "wants to know what is the latest news" "wants to know news from yesterday"


# ===================================================================================================================================


import nltk
import spacy
from nltk.metrics import edit_distance

original_commands = [
    # Weather-related commands
    "wants to know what's the weather like now",
    "what's the weather today",
    # News-related commands
    "wants to know what is the latest news",
    "what are the headlines today",
    "what's happening in the world",
    "any breaking news",

    # Music-related commands
    "wants to listen to music",
    "play some music",
    "can you play a song for me",
    "put on some background music",

    # Music player commands
    "wants to open the music player",
    "play music on the music player",
    "open the music player app",

    # Image description commands
    "wants to know what is the description of the image",
    "describe the image to me",
    "what do you see in the picture",

    # Add more commands here if needed
]



def compare(nlp, user_command):
    def lexical_similarity(user_command, original_command):
        return 1 - edit_distance(user_command.lower(), original_command.lower()) / max(len(user_command), len(original_command))
    def semantic_similarity(user_command, original_command):
        user_doc = nlp(user_command)
        original_doc = nlp(original_command)
        return user_doc.similarity(original_doc)
    def combined_similarity(user_command, original_commands):
        max_lexical_similarity = 0
        max_semantic_similarity = 0
        best_match_command = None
        for original_command in original_commands:
            lexical_sim = lexical_similarity(user_command, original_command)
            semantic_sim = semantic_similarity(user_command, original_command)
            combined_sim = 0.6 * lexical_sim + 0.4 * semantic_sim
            if combined_sim > max_lexical_similarity:
                max_lexical_similarity = combined_sim
                max_semantic_similarity = semantic_sim
                best_match_command = original_command
        return best_match_command, max_lexical_similarity, max_semantic_similarity
    best_match_command, lexical_sim, semantic_sim = combined_similarity(user_command, original_commands) 
    if lexical_sim >= 0.69 and semantic_sim >= 0.69:
        return best_match_command, True
    else:
        return best_match_command, False   


# nltk.download('punkt')
# nlp = spacy.load("en_core_web_lg")
# import time
# while True:
#     qu = input(">>> ")
#     start_time = time.time()
#     print(compare(nlp, qu))
#     end_time = time.time()
#     e_time = end_time-start_time
#     print(f"{e_time:.4f}")


# ===================================================================================================================================

