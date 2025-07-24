from utils.pocketflow import AsyncNode
from utils.stocks_utils import StockHandler

class TextCaptureNode(AsyncNode):
    async def prep_async(self,shared):
        shared['stock_name']=input('Enter the stock name : ')
        shared['number_of_shares_to_be_bought_or_sold']=input("Enter the number of shares to be bought or sold ")
        shared['cash_reserve']=input("Enter the cash reserve ")
        shared['current_number_of_shares']=input("Enter the current number of shares you are having")
        shared['avg_purchase_price']=input("Enter the average purchase price of the share ")
        return shared['stock_name']
    async def exec_async(self,prep_res):
        stocks=StockHandler(prep_res)
        stock_symbol=await stocks.get_stock_symbol()
        current_price=stocks.get_curr_price()
        return stock_symbol,current_price

    async def post_async(self,shared,prep_res,exec_res):
        stock_symbol,current_price=exec_res
        if prep_res is None or exec_res is None:
            return None
        shared['stock_symbol']=stock_symbol
        shared['current_price']=round(current_price,2)
        
    

