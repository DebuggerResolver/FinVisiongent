import aiohttp
import asyncio
import logging
import yfinance as yf
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime, timedelta

logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class StockHandler:
    def __init__(self,stock_name):
        self.stock_name=stock_name
        self.symbol=None
        
    async def get_stock_symbol(self):
        url = "https://connects.torusdigital.com/api/v1/stocks"
        params = {"query": self.stock_name, "page": 1, "limit": 5}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                data = await response.json()
                self.symbol = data[0]['nsesymbol']  # + ".NS"
                return self.symbol
    
    def get_prev_day_news(self):
        all_news=yf.Ticker(self.stock_name).news
        condensed_news=""
        for news in all_news:
            condensed_news+=news['content']['summary']
        return condensed_news
    
    def get_curr_price(self):
        try:
            symbol=self.symbol+".NS"
            # Fetch stock data
            ticker = yf.Ticker(symbol)
            stock_info = ticker.history(period="1d", interval="1m")  # 1-minute interval for live data

            # Check if live price is available
            if not stock_info.empty:
                live_price = stock_info['Close'].iloc[-1]  # Get the most recent price
                return live_price
            else:
                # If no live data, fetch the last close price
                last_close_price = ticker.history(period="1d")['Close'].iloc[-1]
                return last_close_price
        except Exception as e:
            print(f"Error fetching stock price for {self.symbol}: {e}")
            return None
        
    def get_historical_data(self,symbol):
        # Define time range
        end_date = datetime.today().date()
        start_date = end_date - timedelta(days=30)

        # Fetch historical data
        ticker = yf.Ticker(symbol)
        hist = ticker.history(start=start_date, end=end_date)

        # Display result
        if hist.empty:
            print("No data returned. Check ticker symbol or market holidays.")
        else:
            return hist.round(2) 

    
       
    
if __name__=="__main__":
    import asyncio
    stock=StockHandler("Tata Consultancy Services")
    asyncio.run(stock.get_stock_symbol())
    stock.get_prev_day_news()
    print(stock.get_historical_data(stock.symbol))