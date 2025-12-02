import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from .prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE


load_dotenv()  # loads OPENAI_API_KEY from .env if present


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set. Create a .env file from .env.example.")
    return OpenAI(api_key=api_key)


def summarize_boxscore(
    client: OpenAI,
    url: str,
    boxscore_text: str,
    model: str = "gpt-4.1-nano",   # Using 4.1-nano to keep costs miniscule as this is a learning repo
) -> str:
    """
    Call the OpenAI Chat Completions API to summarize an ESPN box score.
    """

    user_prompt = USER_PROMPT_TEMPLATE.format(
        url=url,
        boxscore_text=boxscore_text,
    )

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return response.choices[0].message.content.strip()
