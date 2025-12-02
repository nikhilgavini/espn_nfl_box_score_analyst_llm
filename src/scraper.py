import requests
from bs4 import BeautifulSoup

def fetch_website_contents(url: str, max_chars: int = 8000) -> str:
    """
    Fetch readable text from an ESPN box score page.
    Removes common noise elements and returns clean text.
    """

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch {url}: {e}")

    soup = BeautifulSoup(response.content, "html.parser")

    # Get title if present
    title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"

    # Remove irrelevant tags
    if soup.body:
        for tag in soup.body(["script", "style", "img", "input"]):
            tag.decompose()
        text = soup.body.get_text(separator="\n", strip=True)
    else:
        text = ""

    # Collapse excessive empty lines
    cleaned = "\n".join(
        line.strip()
        for line in text.splitlines()
        if line.strip()
    )

    # Combine title + body
    full_text = f"{title}\n\n{cleaned}"

    # Truncate to avoid blowing token budget
    return full_text[:max_chars]
