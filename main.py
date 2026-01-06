from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agents.crypto_agent import run_crypto_agent
from services.news_service import fetch_crypto_news

app = FastAPI(title="Crypto Analysis AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Crypto Analysis Agent running"}

@app.get("/crypto-news")
def get_news():
    return {"news": fetch_crypto_news()}

# Changed function name to 'run_agent_basic'
@app.get("/run-agent")
def run_agent_basic():
    return run_crypto_agent()

# Changed function name to 'run_deep_analysis'
@app.get("/analyze")
def run_deep_analysis():
    return run_crypto_agent()
