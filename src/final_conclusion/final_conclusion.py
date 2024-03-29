import asyncio
import os
from gpt_json import GPTJSON, GPTMessage, GPTMessageRole
from pydantic import BaseModel, Field

class Conclusion(BaseModel):
    score: int = Field(description="From 0 - 100, how truthfull is the statement?")
    description: str


SYSTEM_PROMPT = """
You will receive a statement and a list of claims. Those claims will have already references and source quotes. Your task is to
evaluate all of this together and provide a comprehensive conclusion. You will provide a score from 0 - 100 how truthfull you
think this statement is and a description of why you think so.

Respond with the following JSON schema:

{json_schema}
"""

async def final_conclusion(investigation_results: str) -> Conclusion:
    gpt_json = GPTJSON[Conclusion](os.getenv("OPENAI_API_KEY"), model=os.getenv("OPENAI_MODEL_CONCLUSION"))
    payload = await gpt_json.run(
        messages=[
            GPTMessage(
                role=GPTMessageRole.SYSTEM,
                content=SYSTEM_PROMPT,
            ),
            GPTMessage(
                role=GPTMessageRole.USER,
                content=investigation_results,
            )
        ]
    )
    return payload.response
