import asyncio
from enum import Enum
import os
from urllib.parse import urlparse
from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel
from factuality.claim_splitter.claim_splitter import Claim
from factuality.search.search import SearchResults
from factuality.utils import logging

logger = logging.get_logger()


class ResultType(Enum):
    VERIFIED = "verified"
    INCONCLUSIVE = "inconclusive"
    REJECTED = "rejected"


class Result(BaseModel):
    result: ResultType
    source_quote: str | None = None


class ClaimChecked(Claim):
    result: ResultType
    source_reference: str | None = None
    source_quote: str | None = None


def split_with_overlap(text, chunk_size, overlap):
    chunks = []
    start = 0
    while start + chunk_size <= len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = start + chunk_size - overlap

    if start < len(text):
        chunks.append(text[start:])
    return chunks


SYSTEM_PROMPT = """
You are a source checker you will try to verify a claim by checking the source. Either you answer with verified, inconclusive or
rejected. For inconclusive you will provide no source quote, for rejected and verified you will provide a source
quoute. Extract the quote directly from the text without modification.

Respond with the following JSON schema:

{json_schema}
"""


async def check_claim(
    claim: Claim,
    sources: list[SearchResults],
    validation_checks_per_claim: int,
    same_site_allowed: bool,
    search_extract_article_length: int,
    search_extract_article_overlap: int,
    oai_key: str,
    oai_model: str,
) -> list[ClaimChecked]:
    claim_checks = []
    sources_used = []
    for source in sources:
        if not same_site_allowed and urlparse(source.url)[1] in sources_used:
            continue
        if validation_checks_per_claim <= len(claim_checks):
            break
        for chunk in split_with_overlap(
            source.text, search_extract_article_length, search_extract_article_overlap
        ):
            try:
                logger.debug(f"Checking claim", claim=claim.claim, source=source.url)
                gpt_json = GPTJSON[Result](oai_key, model=oai_model)
                payload = await gpt_json.run(
                    messages=[
                        GPTMessage(
                            role=GPTMessageRole.SYSTEM,
                            content=SYSTEM_PROMPT,
                        ),
                        GPTMessage(
                            role=GPTMessageRole.USER,
                            content=f"claim: {claim.claim} source: {chunk}",
                        ),
                    ]
                )
                if (
                    payload.response.result == ResultType.REJECTED
                    or payload.response.result == ResultType.VERIFIED
                ) and payload.response.source_quote is not None:
                    logger.debug(
                        f"Claim checked",
                        claim=claim.claim,
                        source=source.url,
                        result=payload.response.result,
                        source_quote=payload.response.source_quote,
                    )
                    sources_used.append(urlparse(source.url)[1])
                    claim_checks.append(
                        ClaimChecked(
                            claim=claim.claim,
                            reference=claim.reference,
                            verification_query=claim.verification_query,
                            result=payload.response.result,
                            source_reference=source.url,
                            source_quote=payload.response.source_quote,
                        )
                    )
                    break
            except Exception as e:
                logger.warning(
                    f"Error checking claim {claim.claim} with source {source.url}: {e}"
                )
                pass
    if len(claim_checks) > 0:
        return claim_checks
    logger.debug(f"Claim checked", claim=claim.claim, result=ResultType.INCONCLUSIVE)
    return [
        ClaimChecked(
            claim=claim.claim,
            reference=claim.reference,
            verification_query=claim.verification_query,
            result=ResultType.INCONCLUSIVE,
            source_reference=None,
            source_quote=None,
        )
    ]
