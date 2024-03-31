from enum import Enum

class Defaults(Enum):
    BING_SEARCH_V7_ENDPOINT = 'https://api.bing.microsoft.com/'
    OPENAI_MODEL_EXTRACT = 'gpt-3.5-turbo'
    OPENAI_MODEL_FACTCHECK = 'gpt-3.5-turbo'
    OPENAI_MODEL_CONCLUSION = 'gpt-3.5-turbo'
    SEARCH_EXTRACT_ARTICLE_LENGTH = 5000
    SEARCH_EXTRACT_ARTICLE_OVERLAP = 500
    MAXIMUM_SEARCH_RESULTS = 5
    SEARCH_ENGINE = 'bing'
    OUTPUT_FORMAT = 'console'
    OUTPUT_PATH = '.'
    ALLOWLIST = '[]'
    BLOCKLIST = '[]'
    VALIDATION_CHECKS_PER_CLAIM = 1
    SAME_SITE_ALLOWED = True