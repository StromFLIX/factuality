from enum import Enum
from typing import Literal
from factuality.search.bing.bing_search import BingSearchClient
from newspaper import Article
from pydantic import BaseModel
from factuality.search.google.google_search import GoogleSearchClient
from factuality.utils import logging
from urllib.parse import urlparse

from factuality.utils.options import Options

logger = logging.get_logger()


class SearchResults(BaseModel):
    url: str
    text: str


class SearchClient:
    def search(
        self, search_engine: Literal["google", "bing"], query, options: Options
    ) -> list[SearchResults]:
        logger.debug(f"Searching for query", query=query, search_engine=search_engine)
        search_results = []
        if search_engine == "bing":
            search_results_raw = BingSearchClient(
                options.bing_search_v7_subscription_key, options.bing_search_v7_endpoint
            ).search(
                query,
                options.maximum_search_results,
                options.allowlist,
                options.blocklist,
            )
            search_results = [
                {"url": search_result["url"], "title": search_result["name"]}
                for search_result in search_results_raw["webPages"]["value"]
            ]
        elif search_engine == "google":
            search_results_raw = GoogleSearchClient(
                options.google_search_api_key, options.google_search_cx
            ).search(
                query,
                options.maximum_search_results,
                options.allowlist,
                options.blocklist,
            )
            search_results = [
                {"url": search_result["link"], "title": search_result["title"]}
                for search_result in search_results_raw["items"]
                if search_result.get("fileFormat") is None
            ]
        else:
            raise ValueError(f"No loader found for search_engine type: {search_engine}")
        search_results_txt = []
        search_results_log = [
            {"domain": urlparse(result["url"])[1], "title": result["title"]}
            for result in search_results
        ]
        logger.debug(f"Search results found", search_results=search_results_log)
        for search_result in search_results:
            url = search_result["url"]
            logger.debug(f"Downloading article from url", url=url)
            article = Article(url)
            try:
                article.download()
                article.parse()
                search_results_txt.append(SearchResults(text=article.text, url=url))
                logger.debug(f"Downloaded article successfully from url", url=url)
            except Exception as e:
                logger.warning(f"Error downloading article {url}: {e}")
        return search_results_txt
