
def news_prompt(ticker,news_data):
    return f"""Analyze the following financial news about {ticker} and provide a concise summary focused on potential trading implications:
    
    1. Summarize the key points in 5-6 sentences, highlighting any information that could impact {ticker}’s stock price in the short term.
    
    2. Identify any positive and negative factors mentioned in the news.
    
    3. Based on this news, would you expect the overall sentiment towards {ticker} stock to be bullish, bearish, or neutral? Briefly explain why.
    
    News data: {news_data}
    
    Please provide your analysis in a clear, concise manner.
 """