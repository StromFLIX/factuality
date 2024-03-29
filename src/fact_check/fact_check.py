import asyncio
from enum import Enum
import os
from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel
from claim_splitter.claim_splitter import Claim
from search.search import SearchResults

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

async def check_claim(claim : Claim, sources: list[SearchResults]) -> ClaimChecked:
    for source in sources:
        for chunk in split_with_overlap(source.text, int(os.environ['SEARCH_EXTRACT_ARTICLE_LENGTH']) , int(os.environ['SEARCH_EXTRACT_ARTICLE_OVERLAP'])):
            try:
                gpt_json = GPTJSON[Result](os.getenv("OPENAI_API_KEY"), model=os.getenv("OPENAI_MODEL_FACTCHECK"))
                payload = await gpt_json.run(
                    messages=[
                        GPTMessage(
                            role=GPTMessageRole.SYSTEM,
                            content=SYSTEM_PROMPT,
                        ),
                        GPTMessage(
                            role=GPTMessageRole.USER,
                            content=f"claim: {claim.claim} source: {chunk}",
                        )
                    ]
                )
                if (payload.response.result == ResultType.REJECTED or payload.response.result == ResultType.VERIFIED) and payload.response.source_quote is not None:
                    return ClaimChecked(
                        claim=claim.claim,
                        reference=claim.reference,
                        verification_query=claim.verification_query,
                        result=payload.response.result,
                        source_reference=source.url,
                        source_quote=payload.response.source_quote
                    )
            except Exception as e:
                print(e)
                pass
    return ClaimChecked(
                claim=claim.claim,
                reference=claim.reference,
                verification_query=claim.verification_query,
                result=ResultType.INCONCLUSIVE,
                source_reference=None,
                source_quote=None
            )



