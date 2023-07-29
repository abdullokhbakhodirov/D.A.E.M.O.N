from Chatbot.chat_gpt import gpt_turbo
from Chatbot.unique_code import get_unique_code_from_file, checking
from Chatbot.pgadmin import add_data2


def chatgpt(question):
    count = checking(get_unique_code_from_file())
    answer = gpt_turbo(question, get_unique_code_from_file())
    count += 1
    add_data2(str(count), get_unique_code_from_file())
    return answer
