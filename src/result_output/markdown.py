from pytablewriter import MarkdownTableWriter

from fact_check.fact_check import ClaimChecked
from final_conclusion.final_conclusion import Conclusion

def convert_claims_markdown_table(claimchecks: list[ClaimChecked]) -> str:
    value_matrix = []
    for claimcheck in claimchecks:
        value_matrix.append([claimcheck.claim, claimcheck.result, claimcheck.source_reference, claimcheck.source_quote])

    writer = MarkdownTableWriter(
        table_name="Claim Checked",
        headers=["Claim", "Result", "Source Reference", "Source Quote"],
        value_matrix=value_matrix
    )
    return writer.dumps()

def output_markdown(claimchecks: list[ClaimChecked], statement: str, conclusion: Conclusion | None) -> str:
    output = f"""
    > {statement} 
    {convert_claims_markdown_table(claimchecks)}
    """
    if conclusion is not None:
        output += f"""
        > 🤖 Conclusion [{conclusion.score}/100]: {conclusion.description}
        """
    return output