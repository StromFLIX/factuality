import os
import requests


class GoogleSearchClient:
    def __init__(self):
        self.api_key = os.environ["GOOGLE_SEARCH_API_KEY"]
        self.search_engine_id = os.environ["GOOGLE_SEARCH_ENGINE_ID"]

    def search(self, query, maximum_search_results, allowlist, blocklist):
        """
        Search for a query string using Google Search API.

        Parameters:
        query (str): The search query.

        Returns:
        dict: The JSON response from the API.
        """
        q = query
        params = {
            "num": maximum_search_results,
            "key": self.api_key,
            "cx": self.search_engine_id,
        }
        if len(allowlist) > 0:
            q += " " + " OR ".join(map(lambda x: f"site:{x}", allowlist))
        elif len(blocklist) > 0 and len(allowlist) == 0:
            q += " " + " OR ".join(map(lambda x: f"-site:{x}", blocklist))

        params["q"] = q
        try:
            response = requests.get(
                "https://www.googleapis.com/customsearch/v1", params=params
            )
            response.raise_for_status()

            return response.json()
        except Exception as ex:
            raise ex
