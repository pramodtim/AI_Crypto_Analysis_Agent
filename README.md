# AI_Crypto_Analysis_Agent
🤖 Deep-Crypto-Insight: Agentic Market Analyst
Deep-Crypto-Insight is a multi-stage AI agent designed to move beyond simple news aggregation. It performs high-fidelity market reasoning by synthesizing real-time RSS news feeds with live price action data to generate professional-grade financial reports and future price predictions.

🌟 Key Features
📰 Real-Time Intelligence: Automatically aggregates high-signal news from Coindesk, Cointelegraph, and Decrypt.

📈 Market-Aware Reasoning: Integrates live 7-day price trends and volatility metrics (BTC, ETH, SOL) via Yahoo Finance.

🧠 Multi-Step Analysis:

Synthesis: Correlates specific news events with observed price movements.

Risk Assessment: Identifies Macro, Technical, and Regulatory threats.

Forecasting: Generates "If-Then" prediction scenarios with confidence scoring.

⚡ High-Speed Inference: Powered by Groq using the Llama-3.3-70B model for near-instant deep reasoning.

🏗️ Project Structure
Plaintext

├── agents/
│   └── crypto_agent.py      # Orchestrator: Coordinates data & analysis
├── prompts/
│   ├── analysis_prompt.txt  # Senior Analyst persona & reasoning logic
│   └── prediction_prompt.txt # Forecasting & scenario-modeling logic
├── services/
│   ├── news_service.py      # RSS pipeline for crypto news
│   ├── market_service.py    # Real-time price data (yfinance)
│   └── analysis_service.py  # LLM integration & prompt chaining
├── utils/
│   └── llm_client.py        # Optimized Groq API client
└── main.py                  # FastAPI Entry Point
🚀 Getting Started
Prerequisites
Python 3.10+

Groq API Key

Installation
Clone the repo:

Bash

git clone https://github.com/yourusername/deep-crypto-insight.git
cd deep-crypto-insight
Install dependencies:

Bash

pip install -r requirements.txt
Configure Environment: Create a .env file in the root:

Code snippet

GROQ_API_KEY=your_key_here
Running Locally
Bash

uvicorn main:app --reload
Access the analysis report at: http://127.0.0.1:8000/analyze

📊 Sample Output
Market Sentiment: Bullish (72/100)

Analysis: BTC's 5% jump correlates with the recent ETF spot inflow news. However, high volatility in SOL suggests a "wait-and-see" approach for altcoins.

Prediction: If BTC holds the $94k support level, we expect a retest of $100k within 7 days. Confidence: High.

🛠️ Tech Stack
Framework: FastAPI

AI Model: Llama-3.3-70B (Groq)

Data Sources: yfinance, Feedparser (RSS)

Environment: Render (Deployment)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
