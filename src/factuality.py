import os
from final_conclusion.final_conclusion import Conclusion
from fact_check.fact_check import ClaimChecked, check_claim
from statement_loader.statement_loader import SourceType, StatementLoader
from claim_splitter import claim_splitter
from search.search import SearchClient
from result_output.markdown import output_markdown
from final_conclusion.final_conclusion import final_conclusion
from utils.options import Options
import asyncio


class Factuality:
    def __init__(self, options: Options):
        self.options = options

    def check(self, pathOrText: str) -> tuple[Conclusion, list[ClaimChecked], str]:
        if os.path.isfile(pathOrText):
            source_type = SourceType.TXT
            source = pathOrText

        loader = StatementLoader()

        statement = loader.load_statement(source_type, source)
        claims = asyncio.run(
            claim_splitter.extract_claims(
                statement, self.options.oai_api_key, self.options.openai_model_extract
            )
        )
        results: list[ClaimChecked] = []
        for claim in claims:
            search_client = SearchClient()
            search_results = search_client.search(
                self.options.search_engine,
                claim.claim,
                self.options,
            )
            checked_claim = asyncio.run(
                check_claim(
                    claim,
                    search_results,
                    self.options.validation_checks_per_claim,
                    self.options.same_site_allowed,
                    self.options.search_extract_article_length,
                    self.options.search_extract_article_overlap,
                    self.options.oai_api_key,
                    self.options.openai_model_factcheck,
                )
            )
            results += checked_claim

        final_conclusion_result = asyncio.run(
            final_conclusion(
                output_markdown(results, statement, None),
                self.options.oai_api_key,
                self.options.openai_model_conclusion,
            )
        )
        return (final_conclusion_result, results, statement)

    def convert_conclusions_to_markdown(
        self,
        results: list[ClaimChecked],
        statement: str,
        final_conclusion_result: Conclusion,
    ):
        return output_markdown(results, statement, final_conclusion_result)
