import textwrap
from pytablewriter import MarkdownTableWriter

from factuality.fact_check.fact_check import ClaimChecked
from factuality.final_conclusion.final_conclusion import Conclusion

def convert_claims_markdown_table(claimchecks: list[ClaimChecked]) -> str:
    value_matrix = []
    for claimcheck in claimchecks:
        value_matrix.append([claimcheck.claim, claimcheck.result, claimcheck.source_reference, claimcheck.source_quote])

    writer = MarkdownTableWriter(
        headers=["Claim", "Result", "Source Reference", "Source Quote"],
        value_matrix=value_matrix
    )
    return writer.dumps()

def output_markdown(claimchecks: list[ClaimChecked], statement: str, conclusion: Conclusion | None) -> str:
    quote_formatted = "\n".join([f"> {line}" for line in statement.splitlines()])
    table_formatted = convert_claims_markdown_table(claimchecks)
    output = f"{quote_formatted}\n\n{table_formatted}"

    if conclusion is not None:
        output += f"\n\n> 🤖 Conclusion [{conclusion.score}/100]: {conclusion.description}"
    return output