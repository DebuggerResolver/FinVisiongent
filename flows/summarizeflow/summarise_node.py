from utils.pocketflow import AsyncNode
from utils.stocks_utils import StockHandler
from prompts.summarise_news import news_prompt

from utils.llm import make_llm_call

class SummarizeNode(AsyncNode):
    async def prep_async(self,shared):
        if "stock_symbol" not in shared:
            return None
        return f"{shared['stock_symbol']}.NS"
    
    async def exec_async(self,prep_res):
        stocks=StockHandler(prep_res)
        news=stocks.get_prev_day_news()
        prompt=news_prompt(prep_res,news)
        summarise_news=await make_llm_call(prompt)
        short_medium_term_data=stocks.get_historical_data(prep_res)
        return summarise_news,short_medium_term_data
    
    async def post_async(self,shared,prep_res,exec_res):
        stock_news,short_medium_term_data=exec_res
        shared['stock_news']=stock_news
        shared['short_medium_term_data']=short_medium_term_data
        
    
    