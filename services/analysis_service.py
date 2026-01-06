from utils.llm_client import get_groq_client
from pathlib import Path

client = get_groq_client()
BASE_DIR = Path(__file__).parent.parent
ANALYSIS_PROMPT_PATH = BASE_DIR / "prompts" / "analysis_prompt.txt"
PREDICTION_PROMPT_PATH = BASE_DIR / "prompts" / "prediction_prompt.txt"

def perform_deep_analysis(news_articles: list, market_data: str) -> str:
    # 1. Format News for LLM
    news_text = "\n".join([f"- {a['title']}" for a in news_articles])
    
    # 2. Run Deep Analysis
    analysis_template = ANALYSIS_PROMPT_PATH.read_text(encoding="utf-8")
    analysis_prompt = analysis_template.format(news_text=news_text, market_data=market_data)
    
    analysis_res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": analysis_prompt}],
        temperature=0.2
    )
    analysis_report = analysis_res.choices[0].message.content

    # 3. Run Prediction based on that analysis
    prediction_template = PREDICTION_PROMPT_PATH.read_text(encoding="utf-8")
    prediction_prompt = prediction_template.format(analysis_report=analysis_report)
    
    prediction_res = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prediction_prompt}],
        temperature=0.5 # Slightly higher for "modeling" scenarios
    )
    prediction_report = prediction_res.choices[0].message.content

    return f"{analysis_report}\n\n---\n## MARKET PREDICTIONS\n{prediction_report}"