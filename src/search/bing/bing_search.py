import os
import requests

class BingSearchClient:
    def __init__(self, subscription_key, endpoint):
        self.subscription_key = subscription_key
        self.endpoint = endpoint + "/v7.0/search"

    def search(self, query, maximum_search_results, allowlist, blocklist):
        """
        Search for a query string using Bing Search API.

        Parameters:
        query (str): The search query.
        market (str): The market where the results come from. Default is 'en-US'.

        Returns:
        dict: The JSON response from the API.
        """
        params = {'mkt': "en-us", 'count': maximum_search_results}
        headers = {'Ocp-Apim-Subscription-Key': self.subscription_key}

        q = query
        if len(allowlist) > 0:
            q += " " + " OR ".join(map(lambda x: f"site:{x}", allowlist))
        elif len(blocklist) > 0 and len(allowlist) == 0:
            q += " " + " OR ".join(map(lambda x: f"-site:{x}", blocklist))
        params['q'] = q

        try:
            response = requests.get(self.endpoint, headers=headers, params=params)
            response.raise_for_status()

            return response.json()
        except Exception as ex:
            raise ex
