from utils.pocketflow import Flow
from .summarise_node import SummarizeNode
import numpy as np

def orchestrate():
    summarizer=SummarizeNode()
    shared={'input_type': 'text', 'stock_name': 'reliance', 'number_of_shares_to_be_bought_or_sold': '15', 'cash_reserve': '100000', 'current_number_of_shares': '25', 'avg_purchase_price': '1200', 'stock_symbol': 'RELIANCE', 'current_price': np.float64(1425.0)}
    flow=Flow(start=summarizer)
    flow.run(shared=shared)
    print("SHARE")
    print(shared)

    
if __name__=="__main__":
    orchestrate()
