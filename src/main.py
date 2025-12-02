import argparse
import sys

from .scraper import fetch_website_contents
from .llm_client import get_client, summarize_boxscore


def analyze_boxscore(url: str) -> str:
    """
    High-level pipeline:
    1. Fetch ESPN NFL box score page
    2. Pass to LLM client for analysis
    3. Return concise summary
    """
    print(f"[info] Fetching box score from: {url}", file=sys.stderr)
    boxscore_text = fetch_website_contents(url)

    client = get_client()
    print("[info] Calling LLM...", file=sys.stderr)
    summary = summarize_boxscore(client, url, boxscore_text)

    return summary


def cli() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize an ESPN NFL box score using an OpenAI LLM sports analyst."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="ESPN NFL game URL, e.g. https://www.espn.com/nfl/game/_/gameId/401772894/rams-panthers",  # Chose this game as the example because I was there!
    )

    args = parser.parse_args()

    try:
        summary = analyze_boxscore(args.url)
        print("\n===== LLM ANALYSIS =====\n")
        print(summary)
    except Exception as e:
        print(f"[error] {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    cli()
