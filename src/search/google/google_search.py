import os
import requests

class GoogleSearchClient:
    def __init__(self):
        self.api_key = os.environ['GOOGLE_SEARCH_API_KEY']
        self.search_engine_id = os.environ['GOOGLE_SEARCH_ENGINE_ID']

    def search(self, query):
        """
        Search for a query string using Google Search API.

        Parameters:
        query (str): The search query.

        Returns:
        dict: The JSON response from the API.
        """
        params = {'q': query, 'num': os.environ['MAXIMUM_SEARCH_RESULTS'], 'key': self.api_key, 'cx': self.search_engine_id}

        try:
            response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
            response.raise_for_status()

            return response.json()
        except Exception as ex:
            raise ex
