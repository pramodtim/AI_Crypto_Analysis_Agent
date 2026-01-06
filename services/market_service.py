import yfinance as yf

def fetch_market_data(symbols=["BTC-USD", "ETH-USD", "SOL-USD"]):
    context = "CURRENT MARKET DATA (Last 7 Days):\n"
    for symbol in symbols:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="7d")
        if hist.empty: continue
        
        current_price = hist['Close'].iloc[-1]
        start_price = hist['Close'].iloc[0]
        change_pct = ((current_price - start_price) / start_price) * 100
        volatility = hist['Close'].std()
        
        context += f"- {symbol}: ${current_price:.2f} ({change_pct:+.2f}% 7d change). Volatility: {volatility:.2f}\n"
    return context