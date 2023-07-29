from __future__ import print_function
import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def img_descripte():
    configuration = cloudmersive_image_api_client.Configuration()
    configuration.api_key['Apikey'] = 'f85800e4-d6e8-4d44-8570-b20aea002cd8'
    api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
    root = Tk()
    root.withdraw()
    file_path = askopenfilename()
    image_file = file_path 
    try:
        api_response = api_instance.recognize_describe(image_file)
        a1 = (vars(api_response))['_runner_up_outcome']
        a2 = ((vars(api_response))['_best_outcome'])
        return (vars(a1))['_description'], (vars(a2))['_description']
    except ApiException as e:
        print("Exception when calling RecognizeApi->recognize_describe: %s\n" % e)
        return False

# tuple_ = img_descripte()
# print(tuple_[0], tuple_[1])
