import asyncio
import os
from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel, Field

class Claim(BaseModel):
    claim: str
    reference: str | None = None
    verification_query: str 

class ClaimsArray(BaseModel):
    claims: list[Claim]


SYSTEM_PROMPT = """
You are an claim extractor. You are given a piece of text and you need to extract the references and claims from it. If there are
no references please provide None. Also afterwards provide a verification query to find search results on gooogle or bing to
verify the claim.

Respond with the following JSON schema:

{json_schema}
"""

async def extract_claims(text: str) -> list[Claim]:
    gpt_json = GPTJSON[ClaimsArray](os.getenv("OPENAI_API_KEY"), model=os.getenv("OPENAI_MODEL_EXTRACT")) # gpt-4-turbo-preview
    payload = await gpt_json.run(
        messages=[
            GPTMessage(
                role=GPTMessageRole.SYSTEM,
                content=SYSTEM_PROMPT,
            ),
            GPTMessage(
                role=GPTMessageRole.USER,
                content=text,
            )
        ]
    )
    return payload.response.claims
