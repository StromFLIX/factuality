from enum import Enum
from search.bing.bing_search import BingSearchClient
from newspaper import Article
from pydantic import BaseModel
from utils import logging
from urllib.parse import urlparse
logger = logging.get_logger()

    
class SearchEngineType(Enum):
    GOOGLE = 'google'
    BING = 'bing'

class SearchResults(BaseModel):
    url: str
    text: str

class SearchClient:
    def search(self, search_engine: SearchEngineType, query, market='en-US') -> list[SearchResults]:
        logger.debug(f"Searching for query", query=query, search_engine=search_engine.value)
        search_results = []
        if search_engine == SearchEngineType.BING:
            search_results = BingSearchClient().search(query, market)
        elif search_engine == SearchEngineType.GOOGLE:
            raise NotImplementedError("SearchEngine for Google is not implemented yet.")
        else:
            raise ValueError(f"No loader found for search_engine type: {search_engine}")
        search_results_txt = []
        search_results_log = [
            {"domain": urlparse(result['url'])[1], "title": result['name']}
            for result in search_results['webPages']['value']
        ]
        logger.debug(f"Search results found", search_results=search_results_log)
        for web_page in search_results['webPages']['value']:
            url = web_page['url']
            logger.debug(f"Downloading article from url", url=url)
            article = Article(url)
            try:
                article.download()
                article.parse()
                search_results_txt.append(
                    SearchResults(
                        text=article.text,
                        url=url
                        ))
                logger.debug(f"Downloaded article successfully from url", url=url)
            except Exception as e:
                logger.warning(f"Error downloading article {url}: {e}")
        return search_results_txt
