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

@app.get("/run-agent")
def run_agent():
    return run_crypto_agent()


# In your main.py - The text inside the @app.get() is your URL path
@app.get("/analyze")  # This means you visit /analyze
def run_agent():
    return run_crypto_agent()


