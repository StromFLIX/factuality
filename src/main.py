
import asyncio
from dotenv import load_dotenv

from fact_check import fact_check
from statement_loader.statement_loader import SourceType, StatementLoader
from claim_splitter import claim_splitter
from search.search import SearchEngineType, SearchClient
from result_output.markdown import output_markdown
from final_conclusion.final_conclusion import final_conclusion

load_dotenv()


loader = StatementLoader()

# Loading a statement from a TXT file
source_type = SourceType.TXT
source = "data/obama_no_citizen.txt"
statement = loader.load_statement(source_type, source)
claims = asyncio.run(claim_splitter.extract_claims(statement))
results = []
for claim in claims:
    search_client = SearchClient()
    search_results = search_client.search(SearchEngineType.BING, claim.claim)
    results.append(asyncio.run(fact_check.check_claim(claim, search_results)))

final_conclusion_result = asyncio.run(final_conclusion(output_markdown(results, statement, None)))
print(output_markdown(results, statement, final_conclusion_result))