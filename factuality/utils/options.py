from factuality.utils.defaults import Defaults
import json

class Options:
    def __init__(
        self,
        oai_api_key,
        bing_search_v7_subscription_key = None,
        bing_search_v7_endpoint = Defaults.BING_SEARCH_V7_ENDPOINT.value,
        openai_model_extract = Defaults.OPENAI_MODEL_EXTRACT.value,
        openai_model_factcheck = Defaults.OPENAI_MODEL_FACTCHECK.value,
        openai_model_conclusion = Defaults.OPENAI_MODEL_CONCLUSION.value,
        search_extract_article_length = Defaults.SEARCH_EXTRACT_ARTICLE_LENGTH.value,
        search_extract_article_overlap = Defaults.SEARCH_EXTRACT_ARTICLE_OVERLAP.value,
        maximum_search_results = Defaults.MAXIMUM_SEARCH_RESULTS.value,
        output_format = Defaults.OUTPUT_FORMAT.value,
        output_path = Defaults.OUTPUT_PATH.value,
        search_engine = Defaults.SEARCH_ENGINE.value,
        allowlist = Defaults.ALLOWLIST.value,
        blocklist = Defaults.BLOCKLIST.value,
        validation_checks_per_claim = Defaults.VALIDATION_CHECKS_PER_CLAIM.value,
        same_site_allowed = f"{Defaults.SAME_SITE_ALLOWED.value}",
        google_search_api_key = None,
        google_search_cx = None,
    ):
        self.oai_api_key = oai_api_key
        self.bing_search_v7_subscription_key = bing_search_v7_subscription_key
        self.bing_search_v7_endpoint = bing_search_v7_endpoint
        self.openai_model_extract = openai_model_extract
        self.openai_model_factcheck = openai_model_factcheck
        self.openai_model_conclusion = openai_model_conclusion
        self.search_extract_article_length = search_extract_article_length
        self.search_extract_article_overlap = search_extract_article_overlap
        self.maximum_search_results = int(maximum_search_results)
        self.output_format = output_format
        self.output_path = output_path
        self.search_engine = search_engine
        self.allowlist = json.loads(allowlist)
        self.blocklist = json.loads(blocklist)
        self.validation_checks_per_claim = int(validation_checks_per_claim)
        self.same_site_allowed = True if same_site_allowed.lower() == 'true' else False if same_site_allowed.lower() == 'false' else None
        self.google_search_api_key = google_search_api_key
        self.google_search_cx = google_search_cx
