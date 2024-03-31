import os
from dotenv import load_dotenv

from factuality import Factuality
from utils.defaults import Defaults
from utils.options import Options
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Factuality CLI: Fact-check any statement using ChatGPT with integrated search options (Bing or Google). Generates a markdown table summarizing the claim, verification result, source references, and direct quotes from these sources. Designed for quick verification and summarization to assist in distinguishing factual information from misinformation."
    )
    parser.add_argument(
        "--statement",
        type=str,
        help="Statement to fact-check can be text or path to a text file",
        required=True,
    )
    parser.add_argument(
        "--oai-api-key",
        "-oai_key",
        type=str,
        default=os.getenv("OPENAI_API_KEY"),
        help="OpenAI API key",
    )
    parser.add_argument(
        "--bing-search-v7-subscription-key",
        "-bsv7_key",
        type=str,
        default=os.getenv("BING_SEARCH_V7_SUBSCRIPTION_KEY"),
        help="Bing Search V7 Subscription Key",
    )
    parser.add_argument(
        "--bing-search-v7-endpoint",
        "-bsv7_endpoint",
        type=str,
        default=os.getenv("BING_SEARCH_V7_ENDPOINT", Defaults.BING_SEARCH_V7_ENDPOINT.value),
        help="Bing Search V7 Endpoint URL",
    )
    parser.add_argument(
        "--openai-model-extract",
        "-oai_extract",
        type=str,
        default=os.getenv("OPENAI_MODEL_EXTRACT", Defaults.OPENAI_MODEL_EXTRACT.value),
        help="OpenAI Model for Extract",
    )
    parser.add_argument(
        "--openai-model-factcheck",
        "-oai_factcheck",
        type=str,
        default=os.getenv("OPENAI_MODEL_FACTCHECK", Defaults.OPENAI_MODEL_FACTCHECK.value),
        help="OpenAI Model for Fact Check",
    )
    parser.add_argument(
        "--openai-model-conclusion",
        "-oai_conclusion",
        type=str,
        default=os.getenv("OPENAI_MODEL_CONCLUSION", Defaults.OPENAI_MODEL_CONCLUSION.value),
        help="OpenAI Model for Conclusion",
    )
    parser.add_argument(
        "--search-extract-article-length",
        "-sea_length",
        type=int,
        default=os.getenv("SEARCH_EXTRACT_ARTICLE_LENGTH", Defaults.SEARCH_EXTRACT_ARTICLE_LENGTH.value),
        help="Search Extract Article Length",
    )
    parser.add_argument(
        "--search-extract-article-overlap",
        "-sea_overlap",
        type=int,
        default=os.getenv("SEARCH_EXTRACT_ARTICLE_OVERLAP", Defaults.SEARCH_EXTRACT_ARTICLE_OVERLAP.value),
        help="Search Extract Article Overlap",
    )
    parser.add_argument(
        "--maximum-search-results",
        "-max_results",
        type=int,
        default=os.getenv("MAXIMUM_SEARCH_RESULTS", Defaults.MAXIMUM_SEARCH_RESULTS.value),
        help="Maximum Search Results",
    )

    args = parser.parse_args()

    options = Options(
        oai_api_key=args.oai_api_key,
        bing_search_v7_subscription_key=args.bing_search_v7_subscription_key,
        bing_search_v7_endpoint=args.bing_search_v7_endpoint,
        openai_model_extract=args.openai_model_extract,
        openai_model_factcheck=args.openai_model_factcheck,
        openai_model_conclusion=args.openai_model_conclusion,
        search_extract_article_length=args.search_extract_article_length,
        search_extract_article_overlap=args.search_extract_article_overlap,
        maximum_search_results=args.maximum_search_results,
    )

    factuality = Factuality(options)
    conclusion, checked_claims, statement = factuality.check(args.statement)
    markdwon_text = factuality.convert_conclusions_to_markdown(checked_claims, statement, conclusion)
    console = Console()
    console.print(Markdown(markdwon_text))

if __name__ == "__main__":
    main()
