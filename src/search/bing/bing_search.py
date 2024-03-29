import os
import requests

class BingSearchClient:
    def __init__(self):
        # Initialize with your Bing Search API subscription key and endpoint
        self.subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']
        self.endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/v7.0/search"

    def search(self, query, market='en-US'):
        """
        Search for a query string using Bing Search API.

        Parameters:
        query (str): The search query.
        market (str): The market where the results come from. Default is 'en-US'.

        Returns:
        dict: The JSON response from the API.
        """
        params = {'q': query, 'mkt': market, 'count': os.environ['MAXIMUM_SEARCH_RESULTS']}
        headers = {'Ocp-Apim-Subscription-Key': self.subscription_key}

        try:
            response = requests.get(self.endpoint, headers=headers, params=params)
            response.raise_for_status()  # Raises stored HTTPError, if one occurred.

            # Return the parsed JSON response.
            return response.json()
        except Exception as ex:
            raise ex
