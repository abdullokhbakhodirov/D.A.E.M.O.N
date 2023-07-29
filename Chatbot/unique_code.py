import uuid
import os
from Chatbot.pgadmin import getting_data, add_data, add_data2


def write_unique_code_to_file():
    directory_path = 'C:/'
    file_name = 'unique_code.txt'
    file_path = os.path.join(directory_path, file_name)
    unique_code = str(uuid.uuid4())
    with open(file_path, 'w') as file:
        file.write(unique_code)
    return unique_code


def get_unique_code_from_file():
    directory_path = 'C:/unique_code.txt'
    if os.path.exists(directory_path):
        with open(directory_path, 'r') as file:
            unique_code = file.read().strip()
            return unique_code
    else:
        return False


def checking(id):
    responses = (getting_data(id=id))[0][5]
    if int(responses) >= 25:
        add_data('{}', id)
        add_data2('0', id)
        return 0
    else:
        return int(responses)