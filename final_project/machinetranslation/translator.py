import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('RmEUloYJl7e3PWFrotEgmo_-Jrqtym_v_x1khpH73lIg')
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/161e5a17-39c9-47ff-a6d6-1718da9057cc')
def english_to_french (english_text):
#write the code here
    if not english_text:
        return "Enter the English Text"
    translation= language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text
def french_to_english (french_text):
#write the code here
    if not french_text:
        return "Enter the French Text"
    translation= language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
