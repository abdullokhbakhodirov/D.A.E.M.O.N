import openai
import ast
from Chatbot.pgadmin import getting_data, add_data


def remove_quotes(text):
    cleaned_text = text.replace("'", "").replace('"', "")
    return cleaned_text


def extract_dict_from_string(s):
    try:
        result_dict = ast.literal_eval(s)
        if isinstance(result_dict, dict):
            return result_dict
        else:
            raise ValueError("The extracted object is not a dictionary")
    except:
        raise ValueError("Invalid string. Cannot extract a dict from string")
    

def gpt_turbo(question, id):
    name = "DAEMON"
    openai.api_key = "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"
    item = getting_data(id)
    que = item[0][3]
    items = extract_dict_from_string(que)
    list_que = [{"role": "system", "content": f'''You are chatting with {name}. 
                 My name meaning is DAEMON Digital Assistant for Efficient Multimodal Operations and Navigations. Digital Assistant for Efficient Multimodal Operations and Navigation refers to an AI voice assistant designed to handle various modes of interaction and perform tasks efficiently across different domains. 
                 Created by NeuralSage Industry. The name of my creator is Abdullokh. His sister's name is Sabina. But everyone calls her Sabi. He is not very clerever as his brother. Because my creator is very smart'''}, 
                {"role": "user", "content": f"Hello {name}"}, 
                {"role": "system", "content": "Hello! how can I assist you today?"}]
    if len(items) > 0:
        for i in items:
            list_que.append({"role": "user", "content": i})
            list_que.append({"role": "system", "content": items[i]})
    list_que.append({"role": "user", "content": question})
    answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=list_que, 
    )['choices'][0]['message']['content']
    list_que.append({"role": "assistant", "content": answer})
    items[question] = answer
    dict_string = str(items)
    add_data(dict_string, id)
    return remove_quotes(answer)