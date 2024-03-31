import asyncio
import os
from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel, Field
from factuality.utils import logging

logger = logging.get_logger()


class Claim(BaseModel):
    claim: str
    reference: str | None = None
    verification_query: str

    class Config:
        use_enum_values = True


class ClaimsArray(BaseModel):
    claims: list[Claim]


SYSTEM_PROMPT = """
You are an claim extractor. You are given a piece of text and you need to extract the references and claims from it. If there are
no references please provide None. Also afterwards provide a verification query to find search results on gooogle or bing to
verify the claim.

Respond with the following JSON schema:

{json_schema}
"""


async def extract_claims(text: str, oai_key: str, oai_model: str) -> list[Claim]:
    logger.debug(f"Extracting claims from statement", statement=text)
    gpt_json = GPTJSON[ClaimsArray](oai_key, model=oai_model)
    payload = await gpt_json.run(
        messages=[
            GPTMessage(
                role=GPTMessageRole.SYSTEM,
                content=SYSTEM_PROMPT,
            ),
            GPTMessage(
                role=GPTMessageRole.USER,
                content=text,
            ),
        ]
    )
    logger.debug(
        f"Succesfully extracted claims", statement=text, claims=payload.response.claims
    )
    return payload.response.claims
