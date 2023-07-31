import requests

class DictionaryAPI:
    BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"
#create functions to send over info to the gui file
    def get_response(self, word):
        url = self.BASE_URL + word
        response = requests.get(url).json()
        return response

    def get_definition(self, response):
        return response[0]['meanings'][0]['definitions'][0]['definition']

    def get_synonyms(self, response):
        return response[0]['meanings'][0].get('synonyms', [])

    def get_more_info(self, response):
        return response[0]['sourceUrls']


    
    




