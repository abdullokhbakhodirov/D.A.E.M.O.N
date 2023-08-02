# ===================================================================================================================================


# Wheather = "wants to know what's the weather like now", "wants to know what is the wheather for tomorrow", "wants to know what was the whether yesterday or previous days"
# Music = "wants to listen music", "wants to open music player", "open music player"
# Image Description = "wants to know what is the description of the image"
# News = "wants to know what is the latest news" "wants to know news from yesterday"


# ===================================================================================================================================


import nltk
import spacy
from nltk.metrics import edit_distance

commandss = {
    # Weather-related commands
    'weather':[
    "wants to know what's the weather like now",
    "what's the weather today"],

    # News-related commands
    'news':[
    "wants to know what is the latest news",
    "what are the headlines today",
    "what's happening in the world",
    "any breaking news"],

    # Music-related commands
    'music':[
    "wants to listen to music",
    "play some music",
    "can you play a song for me",
    "put on some background music",
    'play a song'],

    # Music player commands
    'player':[
    "wants to open the music player",
    "play music on the music player",
    "open the music player app"],

    # Image description commands
    'img':[
    "wants to know what is the description of the image",
    "describe the image to me",
    "what do you see in the picture"],

    # Add more commands here if needed
    'yes':[
    'Yes',
    'Yes certainly',
    'Yes you can', 
    'Ok', 
    "Ok ask"]
}





def compare(nlp, user_command: str, original_commands:str):
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
    best_match_command, lexical_sim, semantic_sim = combined_similarity(user_command, commandss[original_commands]) 
    if lexical_sim >= 0.69 and semantic_sim >= 0.69:
        return  True
    else:
        return  False   


# nltk.download('punkt')
# nlp = spacy.load("en_core_web_lg")
# import time
# while True:
#     qu = input(">>> ")
#     start_time = time.time()
#     print(compare(nlp, qu, 'music'))
#     end_time = time.time()
#     e_time = end_time-start_time
#     print(f"{e_time:.4f}")


# ===================================================================================================================================


import Levenshtein

def sentence_similarity_levenshtein(sentence1, sentence2):
    distance = Levenshtein.distance(sentence1, sentence2)
    max_length = max(len(sentence1), len(sentence2))
    similarity = 1 - (distance / max_length)
    return similarity

def comparing(sentence):
    commandss = {
        'weather': [
            "wants to know what's the weather like now",
            "what's the weather today"
        ],
        'news': [
            "wants to know what is the latest news",
            "what are the headlines today",
            "what's happening in the world",
            "any breaking news", 
            "What is the latest news",
            "Talk about news", 
            "I want to know about last news"
        ],
        'music': [
            "wants to listen to music",
            "play some music",
            "can you play a song for me",
            "put on some background music",
            'play a song'
        ],
        'player': [
            "wants to open the music player",
            "play music on the music player",
            "open the music player app"
        ],
        'img': [
            "wants to know what is the description of the image",
            "describe the image to me",
            "what do you see in the picture"
        ],
        'yes': [
            'Yes',
            'Yes certainly',
            'Yes you can',
            'Ok',
            "Ok ask", 
            "Yes, I want to know about general news too.",
            "Yes, please tell me about general news as well",
            "Absolutely! I want to know about general news too",
            "Definitely! I'm interested in general news as well",
            "Yes, please! I'm eager to hear about general news too", 
            "Yes I want",
            "Yes print all general news too"
        ]
        # Add more commands here if needed
    }

    max_similarity = 0
    matched_command = None

    for command, sentences in commandss.items():
        for sentence_in_command in sentences:
            similarity = sentence_similarity_levenshtein(sentence, sentence_in_command)
            if similarity > max_similarity:
                max_similarity = similarity
                matched_command = command

    return matched_command


