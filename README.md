# ESPN NFL Box Score Analyst - LLM Learning Project
## What this repo demonstrates:
This repo demonstrates a full LLM engineering workflow: scraping real-world data, preprocessing, structured prompting, and calling OpenAI models to produce domain-specific insights.

## What this project does:
Summarize any ESPN NFL game box score using an LLM acting as a professional sports analyst.

This project:
- Fetches an ESPN NFL game page
- Extracts the page text
- Sends it to an OpenAI model with a carefully written system/user prompt
- Returns a concise, analyst-grade breakdown of the game

### Project Diagram
```arduino
ESPN Box Score URL → scraper.py → cleaned text → OpenAI API → analysis output
```

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/nikhilgavini/espn_nfl_box_score_analyst_llm.git
cd espn_nfl_box_score_analyst_llm
```

### 2. Create a virtual environment
#### Using uv:
```bash
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -e .
```
#### Using pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure your OpenAI API Key
```bash
cp .env.example .env
# then edit .env and fill in OPENAI_API_KEY
```

## Usage
### Run from the CLI
```bash
python -m src.main --url "https://www.espn.com/nfl/game/_/gameId/401772894/rams-panthers"
```
