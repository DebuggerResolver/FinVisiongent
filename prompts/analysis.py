
def analysis_prompt(ticker):

    return f"""Analyze this {ticker} candlestick chart focusing on three trading strategies:
    1. MACD Crossover Strategy
    2. KDJ with RSI Filter Strategy
    For each strategy, provide:
    1. One key market trend observation
    2. One potential trading signal
    Format your response as:
    Strategy 1: [Trend] | [Signal]
    Strategy 2: [Trend] | [Signal]
    Be concise. Limit each observation and signal to 10 words or less.
 """