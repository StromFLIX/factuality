from enum import Enum
from search.bing.bing_search import BingSearchClient
from newspaper import Article
from pydantic import BaseModel

    
class SearchEngineType(Enum):
    GOOGLE = 'google'
    BING = 'bing'

class SearchResults(BaseModel):
    url: str
    text: str

class SearchClient:
    def search(self, search_engine: SearchEngineType, query, market='en-US') -> list[SearchResults]:
        search_results = []
        if search_engine == SearchEngineType.BING:
            search_results = BingSearchClient().search(query, market)
        elif search_engine == SearchEngineType.GOOGLE:
            raise NotImplementedError("SearchEngine for Google is not implemented yet.")
        else:
            raise ValueError(f"No loader found for search_engine type: {search_engine}")
        search_results_txt = []
        for web_page in search_results['webPages']['value']:
            url = web_page['url']
            article = Article(url)
            try:
                article.download()
                article.parse()
                search_results_txt.append(
                    SearchResults(
                        text=article.text,
                        url=url
                        ))
            except Exception as e:
                print(f"Error downloading article {url}: {e}")
        return search_results_txt
