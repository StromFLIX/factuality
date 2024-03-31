from utils.defaults import Defaults

class Options:
    def __init__(
        self,
        oai_api_key,
        bing_search_v7_subscription_key,
        bing_search_v7_endpoint = Defaults.BING_SEARCH_V7_ENDPOINT.value,
        openai_model_extract = Defaults.OPENAI_MODEL_EXTRACT.value,
        openai_model_factcheck = Defaults.OPENAI_MODEL_FACTCHECK.value,
        openai_model_conclusion = Defaults.OPENAI_MODEL_CONCLUSION.value,
        search_extract_article_length = Defaults.SEARCH_EXTRACT_ARTICLE_LENGTH.value,
        search_extract_article_overlap = Defaults.SEARCH_EXTRACT_ARTICLE_OVERLAP.value,
        maximum_search_results = Defaults.MAXIMUM_SEARCH_RESULTS.value,
    ):
        self.oai_api_key = oai_api_key
        self.bing_search_v7_subscription_key = bing_search_v7_subscription_key
        self.bing_search_v7_endpoint = bing_search_v7_endpoint
        self.openai_model_extract = openai_model_extract
        self.openai_model_factcheck = openai_model_factcheck
        self.openai_model_conclusion = openai_model_conclusion
        self.search_extract_article_length = search_extract_article_length
        self.search_extract_article_overlap = search_extract_article_overlap
        self.maximum_search_results = maximum_search_results
