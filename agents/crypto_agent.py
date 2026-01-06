from services.news_service import fetch_crypto_news
from services.market_service import fetch_market_data
from services.analysis_service import perform_deep_analysis

def run_crypto_agent():
    # 1. Gather Data
    news = fetch_crypto_news(limit_per_source=5)
    market_metrics = fetch_market_data()

    if not news:
        return {"error": "No data available"}

    # 2. Perform Deep Analysis
    report = perform_deep_analysis(news, market_metrics)

    return {
        "market_summary": market_metrics,
        "deep_analysis_report": report
    }