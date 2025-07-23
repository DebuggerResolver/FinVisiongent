from utils.pocketflow import Flow
from .analyst_node import TechnicalAnalysis
import numpy as np 
def orchestrate():
    tech_node=TechnicalAnalysis()
    shared={'input_type': 'text', 'stock_name': 'reliance', 'number_of_shares_to_be_bought_or_sold': '15', 'cash_reserve': '100000', 'current_number_of_shares': '25', 'avg_purchase_price': '1200', 'stock_symbol': 'RELIANCE', 'current_price': np.float64(1425.0), 'stock_news': "Here is a concise summary of the financial news about RELIANCE.NS:\n\nThe stock price of Reliance Industries (RELIANCE.NS) fell as much as 3.6% due to uncertainty over a trade deal with the US and concerns about the impact of European Union sanctions on Russian crude imports. Despite posting a 78% surge in first-quarter profit, earnings before interest, taxes, depreciation, and amortization in its key oil-to-chemicals and retail segments came in below analysts' expectations. The company's reliance on Russian crude imports may be affected by new EU sanctions, and it may need to find workarounds to maintain its refining margins. On the positive side, Reliance's digital arm, Jio Platforms, has launched a new virtual desktop service, and the company is looking to increase its petrochemical production capacity to meet growing demand.\n\nPositive factors mentioned in the news include the 78% surge in first-quarter profit, driven by strong growth across key businesses and gains from the sale of its stake in Asian Paints, as well as the launch of Jio Platforms' new virtual desktop service. Negative factors include the drop in stock price, concerns about the impact of EU sanctions on Russian crude imports, and earnings before interest, taxes, depreciation, and amortization coming in below analysts' expectations.\n\nBased on this news, the overall sentiment towards RELIANCE.NS stock is likely to be neutral to bearish in the short term, as the company faces challenges related to trade deals and EU sanctions, which may impact its refining margins and petrochemical production. However, the company's strong profit growth and new business initiatives may help mitigate these challenges and support the stock price in the long term.", 'short_medium_term_data':                             """ Open    High     Low   Close    Volume  Dividends  Stock Splits
Date                                                                                        
2025-06-24 00:00:00+05:30  1465.0  1475.0  1443.1  1450.8  16402744        0.0           0.0
2025-06-25 00:00:00+05:30  1464.0  1472.4  1460.5  1467.3   7525851        0.0           0.0
2025-06-26 00:00:00+05:30  1469.1  1498.8  1465.1  1495.3  14657893        0.0           0.0
2025-06-27 00:00:00+05:30  1499.4  1522.0  1496.9  1515.4  11117052        0.0           0.0
2025-06-30 00:00:00+05:30  1513.8  1524.8  1496.0  1500.6   8409527        0.0           0.0
2025-07-01 00:00:00+05:30  1500.6  1531.4  1500.1  1528.4  10368523        0.0           0.0
2025-07-02 00:00:00+05:30  1528.4  1530.0  1508.7  1518.8   6361002        0.0           0.0
2025-07-03 00:00:00+05:30  1520.8  1531.9  1513.0  1517.8  11283291        0.0           0.0
2025-07-04 00:00:00+05:30  1524.0  1530.0  1517.2  1527.3   6603501        0.0           0.0
2025-07-07 00:00:00+05:30  1526.6  1544.8  1525.0  1541.5   7251074        0.0           0.0
2025-07-08 00:00:00+05:30  1536.0  1544.9  1530.2  1537.6   7171261        0.0           0.0
2025-07-09 00:00:00+05:30  1536.7  1551.0  1510.1  1519.0   8870660        0.0           0.0
2025-07-10 00:00:00+05:30  1519.7  1524.7  1507.5  1517.2  10047129        0.0           0.0
2025-07-11 00:00:00+05:30  1512.0  1515.0  1490.3  1495.2   7234991        0.0           0.0
2025-07-14 00:00:00+05:30  1492.2  1500.0  1479.1  1483.7  10311846        0.0           0.0
2025-07-15 00:00:00+05:30  1486.2  1496.5  1482.4  1485.4   8132454        0.0           0.0
2025-07-16 00:00:00+05:30  1473.0  1491.0  1471.5  1485.6  10409983        0.0           0.0
2025-07-17 00:00:00+05:30  1487.4  1489.6  1473.9  1476.4  11854613        0.0           0.0
2025-07-18 00:00:00+05:30  1484.8  1484.8  1469.1  1476.0  10296318        0.0           0.0
2025-07-21 00:00:00+05:30  1465.0  1476.0  1423.1  1428.6  22442744        0.0           0.0
2025-07-22 00:00:00+05:30  1427.4  1431.9  1410.7  1412.8  20396320        0.0           0.0
2025-07-23 00:00:00+05:30  1426.0  1426.0  1414.4  1424.6   8353220        0.0           0.0"""}
    flow=Flow(start=tech_node)
    flow.run(shared=shared)
    print("SHARED ")
    print(shared)
    
if __name__=="__main__":
    orchestrate()
 